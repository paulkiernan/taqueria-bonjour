# pull official base image
FROM node:13.12.0-alpine

# set working directory
WORKDIR /src

# add `/src/node_modules/.bin` to $PATH
ENV PATH /src/node_modules/.bin:$PATH

# install src dependencies
COPY package*.json ./
RUN npm install
RUN npm install react-scripts@3.4.1 -g

# add src
COPY . ./

# start app
CMD ["yarn", "start"]
