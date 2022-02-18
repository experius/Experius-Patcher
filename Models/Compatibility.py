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
            return False

        if not self.isExperiusPatch(patchNum):
            return False
        
        if not self.compatibilityExists(patchNum):
            return False

        return self.isApplicable(patchNum)
    
    def getPatchNum(self, patch):
        try:
            return patch.split('_')[0]
        except:
            return None

    def isExperiusPatch(self, patchNum):
        return patchNum.lstrip('0').isnumeric()
    
    def compatibilityExists(self, patchNum):
        return (patchNum in self.compatibilityList is not None)
    

    def getModuleVersion(self, module):
        for mod in self.modules:
            if mod['name'] == module:
                return mod['version'].split('-')[0]

        return None

    def isApplicable(self, patchNum):
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

                if min is not None and version.parse(moduleVersion) < version.parse(min):
                    isCompatible = False
                    break
                if max is not None and version.parse(moduleVersion) > version.parse(max):
                    isCompatible = False
                    break
            
            if isCompatible:
                return {'name': module}

        return False
