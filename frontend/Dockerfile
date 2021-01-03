# pull official base image
FROM node:15.4.0-alpine3.10

LABEL org.opencontainers.image.source=https://github.com/paulkiernan/taqueria-bonjour

# set working directory
WORKDIR /src

# add `/src/node_modules/.bin` to $PATH
ENV PATH /src/node_modules/.bin:$PATH

# install src dependencies
COPY package.json ./
COPY yarn.lock ./
RUN yarn install

# add src
COPY . ./

# start app
CMD ["yarn", "start"]
