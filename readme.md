py -m venv .venv

py -m pip install django

django-admin --version

source .venv/Scripts/activate

django-admin startproject config .

pip install django djangorestframework                       `'rest_framework'`(add in installed apps)




Regular-

git add .
git commit -m "ready"
git push

## Vercel deployment

The books API is available at `/api/book/`. Django allows Vercel subdomains by
default; for a custom domain, set `DJANGO_ALLOWED_HOSTS` in the Vercel project
environment variables to a comma-separated list of hostnames.

If a deployment URL redirects to Vercel login/SSO, disable Deployment Protection
for a publicly accessible API or use the project's public production domain.
