from apps.apiv1.resource.Base import BaseView


class IndexView(BaseView):

    @BaseView.auth
    def get(self):
        return {"success": "首页"}