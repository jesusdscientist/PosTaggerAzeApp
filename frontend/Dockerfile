# Use Node.js as a parent image
FROM node:16-alpine as build-stage

# Set the working directory in the container
WORKDIR /app

# Install app dependencies
# A wildcard is used to ensure both package.json AND package-lock.json are copied
# where available (npm@5+)
COPY package*.json ./

# Install any needed packages
RUN npm install

# Bundle app source
COPY . .

# Build the app
RUN npm run build

# Use nginx to serve the React app
FROM nginx:alpine

# Copy the build output to replace the default nginx contents.
COPY --from=build-stage /app/build/ /usr/share/nginx/html

# Expose port 80 to the outside once the container has launched
EXPOSE 80

# Start nginx
CMD ["nginx", "-g", "daemon off;"]
