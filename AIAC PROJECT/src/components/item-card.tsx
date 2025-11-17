import Link from 'next/link';
import Image from 'next/image';
import type { Item } from '@/lib/definitions';
import {
  Card,
  CardContent,
  CardHeader,
  CardTitle,
} from '@/components/ui/card';
import { MapPin } from 'lucide-react';

type ItemCardProps = {
  item: Item;
};

export default function ItemCard({ item }: ItemCardProps) {
  return (
    <Link href={`/items/${item.id}`} className="group">
      <Card className="h-full overflow-hidden transition-all duration-300 ease-in-out group-hover:shadow-lg group-hover:-translate-y-1">
        <CardHeader className="p-0">
          <div className="relative aspect-video w-full">
            <Image
              src={item.imageUrl}
              alt={item.name}
              fill
              className="object-cover"
              sizes="(max-width: 640px) 100vw, (max-width: 1024px) 50vw, 33vw"
              data-ai-hint={item.imageHint}
            />
          </div>
        </CardHeader>
        <CardContent className="p-4 space-y-1">
          <CardTitle className="text-lg font-semibold leading-tight group-hover:text-primary">
            {item.name}
          </CardTitle>
          <div className="flex items-center text-sm text-muted-foreground">
            <MapPin className="mr-1.5 h-4 w-4 flex-shrink-0" />
            <span>{item.location}</span>
          </div>
        </CardContent>
      </Card>
    </Link>
  );
}
