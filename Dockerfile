FROM pypy:3.7

RUN git clone https://github.com/pyenv/pyenv.git ~/.pyenv && \
    echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc && \
    echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc && \
    echo 'eval "$(pyenv init -)"' >> ~/.bashrc && \
    . ~/.bashrc  && \
    pyenv install 3.9.1

WORKDIR /src

COPY src/Pipfile* ./
RUN pip install pipenv && \
    pipenv install

COPY src/requirements.txt .
RUN pip install -r requirements.txt
