from ..DAL.RoleDAL import RoleDAL

class RoleBAL:
    def RoleInsert(self,ProfileId,RoleName):
        objRoleDAL=RoleDAL()
        return objRoleDAL.RoleInsert(ProfileId,RoleName)

    def GetRoleByProfileId(self,ProfileId):
        objRoleDAL=RoleDAL()
        return objRoleDAL.GetRoleByProfileId(ProfileId)

    def GetRoleByRoleId(self,RoleId):
        objRoleDAL=RoleDAL()
        return objRoleDAL.GetRoleByRoleId(RoleId)

    def RoleUpdate(self,RoleId,ProfileId,RoleName):
        objRoleDAL=RoleDAL()
        return objRoleDAL.RoleUpdate(RoleId,ProfileId,RoleName)

    def RoleDelete(self,RoleId):
        objRoleDAL=RoleDAL()
        return objRoleDAL.RoleDelete(RoleId)

        
