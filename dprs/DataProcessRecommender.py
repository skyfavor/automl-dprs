import time
from dprs.common.Singleton import Singleton
from dprs.common.thread.KubePodSafetyTermThread import KubePodSafetyTermThread
from dprs.common.Common import Common
from dprs.manager.DPRSManager import DPRSManager


class DataProcessRecommender(KubePodSafetyTermThread, metaclass=Singleton):
    def __init__(self, job_id: str, job_idx: str):
        KubePodSafetyTermThread.__init__(self)
        self.logger = Common.LOGGER.get_logger()
        self.job_id = job_id

        self.dprs_manager = DPRSManager(job_id, job_idx)

        self.logger.info("DataProcessRecommender Initialized!")

    def run(self) -> None:
        self.dprs_manager.recommender(job_id=self.job_id)
        while not self.dprs_manager.get_terminate():
            time.sleep(10)

        self.logger.info("DataProcessRecommender terminate!")


if __name__ == '__main__':
    import sys

    j_id = sys.argv[1]
    j_idx = sys.argv[2]

    dprs = DataProcessRecommender(j_id, j_idx)
    dprs.start()
    dprs.join()
