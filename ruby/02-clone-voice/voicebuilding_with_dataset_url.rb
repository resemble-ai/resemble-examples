require 'json'
require 'resemble'
require 'pry'

# Make sure you set an environment variable for the RESEMBLE_API_TOKEN, 
# it will be used to initialize the Resemble SDK.
RESEMBLE_API_TOKEN = ENV['RESEMBLE_API_TOKEN'] 

raise StandardError.new("Please set the RESEMBLE_API_KEY environment variable.") if RESEMBLE_API_TOKEN.nil? || RESEMBLE_API_TOKEN.empty?

# Set the API Key for the SDK
Resemble.api_key = RESEMBLE_API_TOKEN

# Here we are choosing what we want to name our voice
voice_name = "Your Voice Clone"

# The dataset is important, is the data that will be used to train our voice. 
# There are two ways to create and train a voice 
#
# 1. Providing a dataset URL; or 
# 2. Uploading individual recordings via the API 
#
# https://docs.app.resemble.ai/docs/resource_voice/create
#
# Ensure that it is public accessible, otherwise, your Voicebuilding may result in 
# an error due to Resemble receiving a Forbidden request on attempt to download.
#
# FIXME: You will need to change this to a url which points to your dataset as a zip file.
#
dataset = 'FIXME: add your dataset URL here!'

puts "Submitting request to Resemble to create a voice: #{voice_name}"

# Submit the request using the creation method
response = Resemble::V2::Voice.create(
  voice_name, 
  dataset
)

# Use the attributes in the response to output to STDOUT
# See the documentation for an overview on the response shape
#
# https://docs.app.resemble.ai/docs/resource_voice/resource
#
if response['success']
  voice = response['item']
  voice_status = voice['status']
  voice_uuid = voice['uuid']

  puts "Response was successful! #{voice_name} has been created with UUID #{voice_uuid}. The voice is currently #{voice_status}."
else 
  puts "Response was unsuccessful!"

  # In case of an error, print the error to STDOUT
  puts response
end

