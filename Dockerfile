from quay.io/pypa/manylinux2014_x86_64:2021-09-12-b124c44
RUN yum update -y && yum install -y mpfr-devel boost-devel emacs
ENV PATH="/opt/python/cp310-cp310/bin:${PATH}"
RUN git clone --recurse-submodules https://github.com/scikit-hep/fastjet && cd fastjet && pip install -e .[test]

