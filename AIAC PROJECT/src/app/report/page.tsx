import ReportItemForm from '@/components/report-item-form';

export default function ReportPage() {
  return (
    <div className="max-w-3xl mx-auto">
      <div className="space-y-2 mb-8 text-center">
        <h1 className="text-3xl font-bold font-headline">Report a Found Item</h1>
        <p className="text-muted-foreground">
          Thank you for helping our community. Please provide as much detail as possible.
        </p>
      </div>
      <ReportItemForm />
    </div>
  );
}
