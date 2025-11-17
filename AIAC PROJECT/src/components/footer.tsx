export default function Footer() {
  return (
    <footer className="bg-card border-t mt-auto">
      <div className="container mx-auto py-4 px-4 sm:px-6 lg:px-8">
        <p className="text-center text-sm text-muted-foreground">
          &copy; {new Date().getFullYear()} SRU Lost &amp; Found. All rights reserved.
        </p>
      </div>
    </footer>
  );
}
