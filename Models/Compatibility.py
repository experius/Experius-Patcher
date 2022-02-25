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
                return mod['version']

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

                baseVersion = moduleVersion.split('-')[0]
                patchVersion = 0
                if len(moduleVersion.split('-')) > 1:
                    patchVersion = int(moduleVersion.split('-')[1].lstrip('p'))

                if min is not None:
                    minBaseVersion = min.split('-')[0]
                    minPatchVersion = 0
                    if len(min.split('-')) > 1:
                        minPatchVersion = int(min.split('-')[1].lstrip('p'))
                    if version.parse(baseVersion) < version.parse(minBaseVersion):
                        isCompatible = False
                        break
                    if baseVersion == minBaseVersion:
                        if patchVersion < minPatchVersion:
                            isCompatible = False
                            break

                if max is not None:
                    maxBaseVersion = max.split('-')[0]
                    maxPatchVersion = 0
                    if len(max.split('-')) > 1:
                        maxPatchVersion = int(max.split('-')[1].lstrip('p'))
                    if version.parse(baseVersion) > version.parse(maxBaseVersion):
                        isCompatible = False
                        break
                    if baseVersion == maxBaseVersion:
                        if patchVersion > maxPatchVersion:
                            isCompatible = False
                            break
            
            if isCompatible:
                return {'name': module}

        return False
