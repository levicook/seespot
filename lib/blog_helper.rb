module BlogHelper
  def articles options={}
    @pages.find(:all,
                :in_directory => options[:in_directory] || SITE.blog_dir,
                :recursive => true, :sort_by => :created_at,
                :extension => 'html', :reverse => true).reject { |page| page.filename == 'index' }
  end
end

Webby::Helpers.register(BlogHelper)
