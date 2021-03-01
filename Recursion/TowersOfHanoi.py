class Solution:
    def Met(self, discs, start, helper, destination):
        if discs == 1:
            print(f"{start} to {destination}")
        else:
            Solution.Met(self,discs-1,start,destination,helper)
            print(f"{start} to {destination}")
            Solution.Met(self,discs-1,helper,start,destination)
