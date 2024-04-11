FROM ubuntu:focal

ARG DEBIAN_FRONTEND=noninteractive

RUN echo "===> Installing system dependencies..." && \
    BUILD_DEPS="curl unzip" && \
    apt-get update && apt-get install --no-install-recommends -y \
    python3 python3-pip wget \
    fonts-liberation libappindicator3-1 libasound2 libatk-bridge2.0-0 \
    libnspr4 libnss3 lsb-release xdg-utils libxss1 libdbus-glib-1-2 libgbm1 \
    $BUILD_DEPS \
    xvfb && \
    \
    \
# настроить динамическую выдачу нужного хромдрайвера
    wget https://storage.googleapis.com/chrome-for-testing-public/123.0.6312.105/linux64/chromedriver-linux64.zip && \
    unzip chromedriver-linux64.zip -d /usr/bin && \
    mv /usr/bin/chromedriver-linux64/chromedriver /usr/bin/chromedriver && \
    rm -rf /usr/bin/chromedriver_linux64 && \
    rm chromedriver-linux64.zip && \
    \
    apt-get install -y libu2f-udev && \
    \
    CHROME_SETUP=google-chrome.deb && \
    wget -O $CHROME_SETUP "https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb" && \
    dpkg -i $CHROME_SETUP && \
    apt-get install -y -f && \
    rm $CHROME_SETUP && \
    \
    \
    echo "===> Installing python dependencies..." && \
    apt-get remove -y $BUILD_DEPS && rm -rf /var/lib/apt/lists/*

COPY . /may_readyscript_test

WORKDIR /may_readyscript_test

RUN pip install --no-cache-dir -r requirements.txt

ENV PYTHONPATH "${PYTHONPATH}:/may_readyscript_test"

CMD tail -f /dev/null
