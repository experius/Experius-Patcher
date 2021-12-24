import json, os
from packaging import version

class Compatibility():
    
    def __init__(self, modules) -> None:
        self.modules = modules
        self.compatibilityList = {}
        with open(os.getcwd() + '/etc/compatibility.json') as compatibilityJson:
            self.compatibilityList = json.load(compatibilityJson)

    def isCompatible(self, patch):
        patchNum = self.getPatchNum(patch)
        
        if patchNum is None:
            return True

        if not self.isExperiusPatch(patchNum):
            return True
        
        if not self.compatibilityExists(patchNum):
            return True

        return self.isCompatible(patchNum)
    
    def getPatchNum(patch):
        try:
            return patch.split('_')[0]
        except:
            return None

    def isExperiusPatch(self, patchNum):
        return patchNum.lstrip('0').isnumeric()
    
    def compatibilityExists(self, patchNum):
        return (self.compatibilityList[patchNum] is not None)
    

    def getModuleVersion(self, module):
        for mod in self.modules:
            if mod['name'] == module:
                return module['version']

        return None

    def isCompatible(self, patchNum):
        for restrictions in self.compatibilityList[patchNum]:
            isCompatible = True
            for module in restrictions:
                if 'min' in restrictions[module]:
                    min = restrictions[module]['min']
                else:
                    min = None
                
                if 'max' in restrictions[module]:
                    max = restrictions[module]['max']
                else:
                    max = None
                    
                if min is None and max is None:
                    continue
                
                moduleVersion = self.getModuleVersion(module)
                if moduleVersion is None:
                    isCompatible = False
                    break
                
                if version.parse(moduleVersion) < version.parse(min) or version.parse(moduleVersion) > version.parse(max):
                    isCompatible = False
                    break
            
            if isCompatible:
                return True

        return False
