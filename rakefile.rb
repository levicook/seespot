load 'tasks/setup.rb'
require 'activesupport'

task :default => :build

task :serve  do
  system 'python "C:\Program Files\Google\google_appengine\dev_appserver.py" output'
end

task :test do
end

desc 'deploy the site to the webserver'
task :deploy => [:clobber, :test, :build] do
  system 'python "C:\Program Files\Google\google_appengine\appcfg.py" update output'
end
