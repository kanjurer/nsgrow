import os
from IPython import get_ipython
from globals import OUTPUT_PATH, CLEAN_UP, AUTO_OUTPUT_FOLDER


def get_filename():
    ip = get_ipython()

    # VSCode setting
    if '__vsc_ipynb_file__' in ip.user_ns:
        return os.path.splitext(os.path.basename(ip.user_ns['__vsc_ipynb_file__']))[0]

    import ipynbname

    return ipynbname.name()


class OutputUtil:
    """
    Output file utility created for managing the output .csv file of each Jupyter notebook.
    clean_up=True will clean up intermediate files and only keep the final output file
    """

    def __init__(self, clean_up=CLEAN_UP) -> None:
        self.filename = get_filename()
        self.__clean_up = clean_up

        self.__output_filepath = os.path.join(OUTPUT_PATH, self.filename)
        self.__count = 0
        self.__history = []

        # make dir if not exists
        if AUTO_OUTPUT_FOLDER and not os.path.exists(OUTPUT_PATH):
            os.mkdir(OUTPUT_PATH)

    def generate_output_filepath(self, desc: str) -> str:
        res = self.__output_filepath + "-" + str(self.__count) + "-" + desc + ".csv"
        self.__count += 1
        self.__history.append(res)

        return res

    def get_curr_filepath(self):
        return self.__history[-1]

    def get_final_filepath(self):
        if self.__clean_up:
            for f in self.__history:
                os.remove(f)

        return self.__output_filepath + ".csv"
