require 'webby'

SITE = Webby.site
SITE.blog_dir = 'public/blog'
SITE.tidy_options = '-indent -wrap 160'
SITE.uv = {
  :lang => 'ruby',
  :theme => 'blackboard',
  :line_numbers => true,
}

# Load the other rake files in the tasks folder
Dir.glob(File.join(%w[tasks *.rake])).sort.each {|fn| import fn}

# Load all the ruby files in the lib folder
Dir.glob(File.join(%w[lib ** *.rb])).sort.each {|fn| require fn}
