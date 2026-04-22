
xxxixx
didid
nxhxnz
xjsjss
sjxdhd8ddhndhssnnsjsfyjvncy
yc77ycdmjsxxnsusnhkaaikakkak
class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        n = len(nums)
        nxt = [-1] * n
        occur = {}
        ans = n + 1
FTC HGBX class Solution {
    public int maxDistance(int[] A, int[] B) {
        int i, j = 1;

        for (i = 0; i < A.length && j < B.length; j++)
            if (A[i] > B[j])
                i++;

        return j - i - 1;
    }
}
        for i in range(n - 1, -1, -1):
            if nums[i] in occur:
                nxt[i] = occur[nums[i]]drt hrhrdg
            occur[nums[i]] = ifv tyghfh t

            hhjbvhcrx
            agadszhadfsHcs
            WAS dvasgvcdf

        for i in range(n):
            second_pos = nxt[i]
            if second_pos != -1:
                third_pos = nxt[second_pos]
                if third_pos != -1:
                    ans = min(ans, third_pos - i)

        return -1 if ans == n + 1 else ans * 2
        class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        n = len(nums)
        ans = n + 1

        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                if nums[i] != nums[j]:
                    continue
                for k in range(j + 1, n):
                    if nums[j] == nums[k]:
                        ans = min(ans, k - i)
                        break

        return -1 if ans == n + 1 else ans * 2




class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        mod = 10**9 + 7
        n = len(nums)
        T = int(n**0.5)

        groups = [[] for _ in range(T)]
        for l, r, k, v in queries:
            if k < T:
                groups[k].append((l, r, v))
            else:
                for i in range(l, r + 1, k):
                    nums[i] = nums[i] * v % mod

        dif = [1] * (n + T)
        for k in range(1, T):
            if not groups[k]:
                continue
            dif[:] = [1] * len(dif)
            for l, r, v in groups[k]:
                dif[l] = dif[l] * v % mod
                R = ((r - l) // k + 1) * k + l
                dif[R] = dif[R] * pow(v, mod - 2, mod) % mod

            for i in range(k, n):
                dif[i] = dif[i] * dif[i - k] % mod
            for i in range(n):
                nums[i] = nums[i] * dif[i] % mod

        res = 0
        for x in nums:
            res ^= x
        return res
        class Solution:
    MOD = 10**9 + 7

    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        for l, r, k, v in queries:
            for i in range(l, r + 1, k):
                nums[i] = (nums[i] * v) % self.MOD

        res = 0
        for x in nums:
            res ^= x

        return resdyudksks
dkjdjddbdjd
ndndidd
djdkdxhjxz
usjs
hug
njj
jjhdjxnd
chchcjd
cjjcxgshwj
xfxks
dod
dhhde

xnxucjnc
dnccj
nshdndnhxhx
class Robot:

    TO_DIR = {
        0: "East",
        1: "North",
        2: "West",
        3: "South",
    }

    def __init__(self, width: int, height: int):
        self.moved = False
        self.idx = 0
        self.pos = list()
        self.dirs = list()

        pos_, dirs_ = self.pos, self.dirs

        for i in range(width):
            pos_.append((i, 0))
            dirs_.append(0)
        for i in range(1, height):
            pos_.append((width - 1, i))
            dirs_.append(1)
        for i in range(width - 2, -1, -1):
            pos_.append((i, height - 1))
            dirs_.append(2)
        for i in range(height - 2, 0, -1):
            pos_.append((0, i))
            dirs_.append(3)

        dirs_[0] = 3

    def step(self, num: int) -> None:
        self.moved = True
        self.idx = (self.idx + num) % len(self.pos)

    def getPos(self) -> List[int]:
        return list(self.pos[self.idx])

    def getDir(self) -> str:
        if not self.moved:
            return "East"
        return Robot.TO_DIR[self.dirs[self.idx]]
hshsns
dbchhdnd
dndhdnd
dgf vvy
ybybtbyn
hdudjs
jrhejrjn
irej
heh
ndjdj
2fndjxx
 rydfs dhtcx h gndc c
 DN dxcB 
 
h rhdudnd
jxjd
b khycfgn jgvy jvbn 
cvgybjyh
Sgj zdkhvx dwr hs f
f keketj
7nybyn
uctryfbTF GK CY
HGGVMKYDV C
5tfu
szgJNBFHISZbFI Stdh j
fcgvhyv
SNBVDZHIBGISABO
"XZFBSIKZBNFOPFw dviy vyigxvgiau i wiyd oby wdog.  idwg. 73. dg ck2 tc
wc hidwyc7 gjc2
2giwit cxfstwgsvssggscbxydbdbsbsgshs x
sbxgsgsbtxdfjnc g
shdxvxvdd
gsgevevegsgegg3g3eysbsh
vgruhdbdasgdzgae s gng nnygfjn
xdfxzhb
 xzdtrjc fbhbfdfcjntcs hb
fhzdhrxhbn fxn  
tgfyuk dfsdcngbngjnghjg
ht dfhg chv mhmk 
lghvjkmnc hvjn

ggjnnbgtdh
ghmv  
