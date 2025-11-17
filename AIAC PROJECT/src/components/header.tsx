import Link from 'next/link';
import { Button } from './ui/button';
import { Search } from 'lucide-react';

export default function Header() {
  return (
    <header className="bg-card border-b sticky top-0 z-50">
      <div className="container mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex items-center justify-between h-16">
          <div className="flex items-center space-x-4">
            <Link href="/" className="flex items-center gap-2 text-primary font-bold text-xl font-headline">
              <Search className="h-6 w-6" />
              <span>SRU Lost &amp; Found</span>
            </Link>
          </div>
          <nav className="hidden md:flex items-center space-x-2">
             <Button variant="ghost" asChild>
              <Link href="/">Dashboard</Link>
            </Button>
            <Button variant="ghost" asChild>
              <Link href="/report">Report Item</Link>
            </Button>
             <Button variant="ghost" asChild>
              <Link href="/admin">Admin</Link>
            </Button>
            <div className="w-px h-6 bg-border mx-2"></div>
            <Button variant="outline" asChild>
              <Link href="/login">Login</Link>
            </Button>
            <Button variant="default" asChild>
              <Link href="/register">Register</Link>
            </Button>
          </nav>
           <div className="md:hidden">
            {/* Mobile menu button could go here */}
          </div>
        </div>
      </div>
    </header>
  );
}
