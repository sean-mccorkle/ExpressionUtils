FROM kbase/kbase:sdkbase2.latest
MAINTAINER KBase Developer
# -----------------------------------------
# In this section, you can install any system dependencies required
# to run your App.  For instance, you could place an apt-get update or
# install line here, a git checkout to download code, or run any other
# installation scripts.

# RUN apt-get update

# Here we install a python coverage tool and an
# https library that is out of date in the base image.

RUN pip install coverage

# Install tablemaker
RUN echo Installing tablemaker \
    && cd /opt \
    && TM_VER='tablemaker-2.1.1.Linux_x86_64' \
    && wget -O ${TM_VER}.tar.gz https://ndownloader.figshare.com/files/3193031 \
    && tar zxvf ${TM_VER}.tar.gz \
    && rm -f ${TM_VER}.tar.gz


# Install gffread
RUN  echo Installing gffread \
  && cd /opt \
  && git clone https://github.com/gpertea/gclib \
  && git clone https://github.com/gpertea/gffread \
  && cd gffread \
  && make

ENV PATH $PATH:/opt/tablemaker-2.1.1.Linux_x86_64:/opt/gffread

# -----------------------------------------

COPY ./ /kb/module
RUN mkdir -p /kb/module/work
RUN chmod -R a+rw /kb/module

WORKDIR /kb/module

RUN make all

ENTRYPOINT [ "./scripts/entrypoint.sh" ]

CMD [ ]
