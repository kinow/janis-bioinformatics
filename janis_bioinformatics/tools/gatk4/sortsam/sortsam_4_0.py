from .base import Gatk4SortSamBase
from ..gatk_4_0_12 import Gatk_4_0_12
from ..gatk_4_1_3_0 import Gatk_4_1_3_0


class Gatk4SortSam_4_0(Gatk_4_0_12, Gatk4SortSamBase):
    pass


class Gatk4SortSam_4_1_3(Gatk_4_1_3_0, Gatk4SortSamBase):
    pass


Gatk4SortSamLatest = Gatk4SortSam_4_1_3

if __name__ == "__main__":
    print(Gatk4SortSam_4_0().help())
