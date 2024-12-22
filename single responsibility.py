class Report:
    def __init__(self, data):
        self.data = data

    def generate_report(self):
        return f"Report Data: {self.data}"

class ReportPrinter:
    def print_report(self, report):
        print(report)
report = Report("Sales Data for 2024")
printer = ReportPrinter()
printer.print_report(report.generate_report())
