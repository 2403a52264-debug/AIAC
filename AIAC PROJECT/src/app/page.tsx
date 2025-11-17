'use client';

import Link from 'next/link';
import { Input } from '@/components/ui/input';
import { Button } from '@/components/ui/button';
import ItemCard from '@/components/item-card';
import { Search, PlusCircle } from 'lucide-react';
import { useItems } from '@/context/ItemsContext';

export default function Home() {
  const { items } = useItems();

  return (
    <div className="space-y-8">
      <div className="text-center p-8 rounded-lg bg-card border shadow-sm">
        <h1 className="font-headline text-4xl md:text-5xl font-bold text-primary">
          SRU Lost &amp; Found
        </h1>
        <p className="mt-2 text-lg text-muted-foreground">
          Your one-stop portal for finding and reporting lost items on campus.
        </p>
        <div className="mt-6 max-w-2xl mx-auto flex gap-2">
          <div className="relative flex-grow">
            <Search className="absolute left-3 top-1/2 -translate-y-1/2 h-5 w-5 text-muted-foreground" />
            <Input
              type="search"
              placeholder="Search for items by keyword, e.g., 'black wallet', 'keys'..."
              className="pl-10 text-base"
            />
          </div>
          <Button type="submit" variant="default">
            Search
          </Button>
        </div>
      </div>

      <div className="flex justify-between items-center">
        <h2 className="text-2xl font-bold font-headline text-primary">Recently Found Items</h2>
        <Button asChild variant="default">
          <Link href="/report">
            <PlusCircle className="mr-2 h-4 w-4" /> Report an Item
          </Link>
        </Button>
      </div>

      <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6">
        {items.map((item) => (
          <ItemCard key={item.id} item={item} />
        ))}
      </div>
    </div>
  );
}
