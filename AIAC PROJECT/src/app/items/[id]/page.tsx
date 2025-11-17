'use client';

import Image from 'next/image';
import { users } from '@/lib/data';
import { useParams, useRouter } from 'next/navigation';
import {
  Card,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from '@/components/ui/card';
import { Badge } from '@/components/ui/badge';
import { Button } from '@/components/ui/button';
import { MapPin, Calendar, User, Tag, Trash2 } from 'lucide-react';
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogFooter,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
  DialogClose,
} from '@/components/ui/dialog';
import {
  AlertDialog,
  AlertDialogAction,
  AlertDialogCancel,
  AlertDialogContent,
  AlertDialogDescription,
  AlertDialogFooter,
  AlertDialogHeader,
  AlertDialogTitle,
  AlertDialogTrigger,
} from "@/components/ui/alert-dialog"
import { Label } from '@/components/ui/label';
import { Input } from '@/components/ui/input';
import { Separator } from '@/components/ui/separator';
import { useToast } from '@/hooks/use-toast';
import { useState, useEffect } from 'react';
import type { Item } from '@/lib/definitions';
import { useItems } from '@/context/ItemsContext';

export default function ItemPage() {
  const params = useParams();
  const router = useRouter();
  const { items, updateItem, deleteItem } = useItems();
  const [item, setItem] = useState<Item | undefined>(undefined);
  
  const { toast } = useToast();
  const [isClaiming, setIsClaiming] = useState(false);
  const [isDialogOpen, setIsDialogOpen] = useState(false);
  
  useEffect(() => {
    if (params.id) {
        const foundItem = items.find((i) => i.id === params.id);
        setItem(foundItem);
    }
  }, [params.id, items]);

  if (!item) {
    // To prevent flashing not found, we can show a loading state
    // Or just return null for a moment
    return null; 
  }

  const getStatusBadge = (status: 'available' | 'claimed' | 'pending') => {
    switch (status) {
      case 'available':
        return <Badge variant="secondary" className="bg-green-200 text-green-900">Available</Badge>;
      case 'claimed':
        return <Badge variant="destructive">Claimed</Badge>;
      case 'pending':
        return <Badge variant="outline" className="bg-yellow-200 text-yellow-900 border-yellow-300">Pending Claim</Badge>;
    }
  };

  const claimant = item.claimedBy ? users.find(u => u.id === item.claimedBy) : null;

  const handleClaimSubmit = (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    setIsClaiming(true);
    
    setTimeout(() => {
        if (item) {
            const updatedItem = { ...item, status: 'pending' as const };
            updateItem(updatedItem); // Update the item in the global context
            setItem(updatedItem); // Update the local state for immediate UI feedback

            toast({
                title: 'Claim Submitted!',
                description: 'Your claim has been submitted for review. You will be notified of the outcome.',
            });
        }
        setIsClaiming(false);
        setIsDialogOpen(false);
    }, 1000);
  }

  const handleDelete = () => {
    if (item) {
      deleteItem(item.id);
      toast({
        title: "Item Deleted",
        description: `${item.name} has been removed from the list.`,
      });
      router.push('/');
    }
  };

  return (
    <div className="max-w-4xl mx-auto">
      <Card className="overflow-hidden">
        <CardHeader className="p-0">
          <div className="relative h-96 w-full">
            <Image
              src={item.imageUrl}
              alt={item.name}
              fill
              className="object-cover"
              data-ai-hint={item.imageHint}
            />
          </div>
        </CardHeader>
        <CardContent className="p-6 grid md:grid-cols-3 gap-6">
          <div className="md:col-span-2 space-y-4">
            <CardTitle className="text-3xl font-headline">{item.name}</CardTitle>
            <div className="flex items-center gap-4 text-muted-foreground">
                {getStatusBadge(item.status)}
                <div className="flex items-center gap-2">
                    <MapPin className="h-4 w-4"/>
                    <span>{item.location}</span>
                </div>
                <div className="flex items-center gap-2">
                    <Calendar className="h-4 w-4"/>
                    <span>Found on {new Date(item.dateFound).toLocaleDateString()}</span>
                </div>
            </div>
            <Separator />
            <CardDescription className="text-base leading-relaxed">{item.description}</CardDescription>
          </div>
          <div className="space-y-4 md:col-span-1">
            <Card className="bg-muted/50">
              <CardHeader>
                <CardTitle className="text-lg font-headline">Item Status</CardTitle>
              </CardHeader>
              <CardContent className="space-y-4">
                <div className="flex items-center gap-3">
                  <Tag className="h-5 w-5 text-primary"/>
                  <div >
                    <p className="font-semibold">Status</p>
                    {getStatusBadge(item.status)}
                  </div>
                </div>
                {item.status === 'claimed' && claimant && (
                  <>
                  <div className="flex items-center gap-3">
                    <User className="h-5 w-5 text-primary"/>
                    <div>
                      <p className="font-semibold">Claimed By</p>
                      <p className="text-sm">{claimant.name}</p>
                    </div>
                  </div>
                   <div className="flex items-center gap-3">
                    <Calendar className="h-5 w-5 text-primary"/>
                    <div>
                      <p className="font-semibold">Claimed On</p>
                      <p className="text-sm">{item.claimedDate ? new Date(item.claimedDate).toLocaleDateString() : 'N/A'}</p>
                    </div>
                  </div>
                  </>
                )}
              </CardContent>
              {item.status === 'available' && (
                <CardFooter className="flex gap-2">
                    <Dialog open={isDialogOpen} onOpenChange={setIsDialogOpen}>
                      <DialogTrigger asChild>
                         <Button className="flex-1 bg-accent text-accent-foreground hover:bg-accent/90">Claim Item</Button>
                      </DialogTrigger>
                      <DialogContent className="sm:max-w-[425px]">
                        <form onSubmit={handleClaimSubmit}>
                          <DialogHeader>
                            <DialogTitle>Claim Item: {item.name}</DialogTitle>
                            <DialogDescription>
                              Please provide your details to initiate the claim. This will be reviewed by an administrator.
                            </DialogDescription>
                          </DialogHeader>
                          <div className="grid gap-4 py-4">
                            <div className="grid grid-cols-4 items-center gap-4">
                              <Label htmlFor="name" className="text-right">
                                Full Name
                              </Label>
                              <Input id="name" placeholder="John Doe" className="col-span-3" required />
                            </div>
                            <div className="grid grid-cols-4 items-center gap-4">
                              <Label htmlFor="username" className="text-right">
                                Student/Faculty ID
                              </Label>
                              <Input id="username" placeholder="S123456" className="col-span-3" required />
                            </div>
                          </div>
                          <DialogFooter>
                            <DialogClose asChild>
                                <Button type="button" variant="ghost">Cancel</Button>
                            </DialogClose>
                            <Button type="submit" variant="default" disabled={isClaiming}>
                                {isClaiming ? 'Submitting...' : 'Submit Claim'}
                            </Button>
                          </DialogFooter>
                        </form>
                      </DialogContent>
                    </Dialog>
                    <AlertDialog>
                      <AlertDialogTrigger asChild>
                        <Button variant="destructive" className="flex-1">
                          <Trash2 className="mr-2 h-4 w-4" /> Delete
                        </Button>
                      </AlertDialogTrigger>
                      <AlertDialogContent>
                        <AlertDialogHeader>
                          <AlertDialogTitle>Are you absolutely sure?</AlertDialogTitle>
                          <AlertDialogDescription>
                            This action cannot be undone. This will permanently delete the
                            item and remove its data from our servers.
                          </AlertDialogDescription>
                        </AlertDialogHeader>
                        <AlertDialogFooter>
                          <AlertDialogCancel>Cancel</AlertDialogCancel>
                          <AlertDialogAction onClick={handleDelete}>Continue</AlertDialogAction>
                        </AlertDialogFooter>
                      </AlertDialogContent>
                    </AlertDialog>
                </CardFooter>
              )}
            </Card>
          </div>
        </CardContent>
      </Card>
    </div>
  );
}
