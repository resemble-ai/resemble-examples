require 'sinatra'
require 'json'
require 'resemble'

# We require an environment variable containing 
# the RESEMBLE_API_TOKEN to be set so that 
# the server and SDK can be initialized properly
RESEMBLE_API_TOKEN = ENV['RESEMBLE_API_TOKEN'] 

raise StandardError.new("Please set the RESEMBLE_API_KEY environment variable.") if RESEMBLE_API_TOKEN.nil? || RESEMBLE_API_TOKEN.empty?

# Set the API Key for the SDK
Resemble.api_key = RESEMBLE_API_TOKEN

# Define a basic Sinatra application server
class MyApp < Sinatra::Base

  # Health check endpoint
  get '/ping' do
    content_type :json
    { message: 'pong' }.to_json
  end

  # Expose an endpoint to clients to fetch all 
  # projects associated
  get '/projects' do
    content_type :json

    # Extract input page and page size 
    # or default if not provided
    page = params[:page] ? params[:page].to_i : 1
    page_size = params[:page_size] ? params[:page_size].to_i : 10

    # Use the SDK to fetch all projects 
    projects = Resemble::V2::Project.all(
      page,
      page_size
    )

    projects.to_json
  end

end

# Run the Sinatra application
MyApp.run!
