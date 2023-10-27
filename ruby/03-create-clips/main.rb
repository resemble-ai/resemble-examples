require 'resemble'
require 'optparse'

# This function sets up the Resemble Ruby SDK
def initialize_resemble_client
  begin
    # Attempt to retrieve the value of the environment variable
    resemble_api_key = ENV['RESEMBLE_API_KEY']

    Resemble.api_key = resemble_api_key
  rescue KeyError
    # If the environment variable is not found, raise an error
    raise EnvironmentError, "The 'RESEMBLE_API_KEY' environment variable is not set."
  end
end

def create_audio_clip(project_uuid, title, body, voice_uuid, is_public = false, is_archived = false)
  puts "Submitting request to Resemble to create audio clip content: #{body}"

  # Make request to the API, note that we do not provide a callback_uri so this
  # request will execute synchronously.
  response = Resemble::V2::Clip.create_sync(
    project_uuid,
    voice_uuid,
    body,
    title: nil,
    sample_rate: nil,
    output_format: nil,
    precision: nil,
    include_timestamps: nil,
    is_public: nil,
    is_archived: nil,
    raw: nil
  )

  if response['success']
    clip = response['item']
    clip_uuid = clip['uuid']
    clip_url = clip['audio_src']

    puts "Response was successful! #{title} has been created with UUID #{clip_uuid}."
    puts clip_url
  else
    puts "Response was unsuccessful!"

    # In case of an error, print the error to STDOUT
    puts response
  end
end

# This is the main function that contains the example
def run_example(arguments)
  # Initialize the client using the environment variable RESEMBLE_API_KEY set
  initialize_resemble_client

  project_uuid = arguments['project_uuid']
  voice_uuid = arguments['voice_uuid']
  title = arguments['title']
  body = arguments['body']
  public = arguments['public']
  archived = arguments['archived']

  # Run the clip creation function to call the Resemble API
  create_audio_clip(
    project_uuid,
    title,
    body,
    voice_uuid,
    public,
    archived
  )
end

options = { "public" => false, "archived" => false}

# Create an option parser
opt_parser = OptionParser.new do |opts|
  opts.banner = "A script that creates static audio content using Resemble AI"

  opts.on('--project_uuid PROJECT_UUID', 'Project UUID to store this clip under') do |project_uuid|
    options['project_uuid'] = project_uuid
  end

  opts.on('--voice_uuid VOICE_UUID', 'Voice UUID to use for this clip content') do |voice_uuid|
    options['voice_uuid'] = voice_uuid
  end

  opts.on('--title TITLE', 'The title of the clip') do |title|
    options['title'] = title
  end

  opts.on('--body BODY', 'The text to synthesize audio content with, can be SSML or plain text') do |body|
    options['body'] = body
  end

  opts.on('--public', 'Set to make public (default: false)') do
    options['public'] = true
  end

  opts.on('--archived', 'Set to archive (default: false)') do
    options['archived'] = true
  end
end

def print_help_and_exit(parser)
  puts "ERR: missing a required argument please check your input and try again."
  puts parser.help
  exit 1
end

opt_parser.parse!

print_help_and_exit(opt_parser) if options['project_uuid'].nil? || options['project_uuid'].empty?
print_help_and_exit(opt_parser) if options['voice_uuid'].nil? || options['voice_uuid'].empty?
print_help_and_exit(opt_parser) if options['title'].nil? || options['title'].empty?
print_help_and_exit(opt_parser) if options['body'].nil? || options['body'].empty?


run_example(options)
