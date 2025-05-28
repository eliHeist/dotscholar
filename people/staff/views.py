from django.shortcuts import render
from django.views import View


class StaffListView(View):
    template_name = 'staff/staff_list.html'

    def get(self, request, *args, **kwargs):
        # Here you would typically fetch staff data from the database
        # For demonstration purposes, we'll use a static list
        staff_members = [
            {'name': 'Alice Smith', 'position': 'Manager'},
            {'name': 'Bob Johnson', 'position': 'Developer'},
            {'name': 'Charlie Brown', 'position': 'Designer'},
        ]
        
        context = {
            'staff_members': staff_members
        }
        
        return render(request, self.template_name, context)

