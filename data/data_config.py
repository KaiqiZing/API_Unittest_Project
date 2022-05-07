# coding=utf-8
class global_var:
    ID="0"
    request_name="1"
    url="2"
    run="3"
    request_way="4"
    header="5"
    case_depend="6"
    data_spend="7"
    field_spend="8"
    data="9"
    except_result="10"
    actual_result="11"

    # 获取以上类变量
    def get_id(self):
        return global_var.ID
    def get_url(self):
        return global_var.url
    def get_run(self):
        return global_var.run
    def get_run_way(self):
        return global_var.request_way
    def get_header(self):
        return global_var.header
    def get_case_depend(self):
        return global_var.case_depend
    def get_data_spend(self):
        return global_var.data_spend
    def get_field_spend(self):
        return global_var.field_spend
    def get_data(self):
        return global_var.data
    def get_except_result(self):
        return global_var.except_result
    def get_actual_result(self):
        return global_var.actual_result

