class BoundApiEndpoint(object):
  def __init__(self, bound_resource, endpoint):
    self.bound_resource = bound_resource
    self.endpoint = endpoint

  def __call__(self, **kwargs):
    name = self.endpoint.name
    url = self.bound_resource.resource._base_url(self.bound_resource.id) + ('/' + name if name else '')
    conn = self.bound_resource.resource.conn
    call = conn._get if self.endpoint.method == 'GET' else conn._post
    raw_response = call(url, kwargs)
    if self.endpoint.response_cls:
      return self.endpoint.response_cls(raw_response)
    else:
      return None


class ApiEndpoint(object):
  def __init__(self, name, response_cls, method):
    self.name = name
    self.response_cls = response_cls
    self.method = method
