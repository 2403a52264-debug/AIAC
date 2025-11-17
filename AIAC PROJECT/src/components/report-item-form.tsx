"use client";

import { zodResolver } from '@hookform/resolvers/zod';
import { useForm } from 'react-hook-form';
import { z } from 'zod';
import { Button } from '@/components/ui/button';
import {
  Form,
  FormControl,
  FormDescription,
  FormField,
  FormItem,
  FormLabel,
  FormMessage,
} from '@/components/ui/form';
import { Input } from '@/components/ui/input';
import { Textarea } from '@/components/ui/textarea';
import { Card, CardContent } from '@/components/ui/card';
import { useState, useTransition } from 'react';
import Image from 'next/image';
import { ImageIcon, Loader2, Sparkles } from 'lucide-react';
import { getImageSuggestions } from '@/app/actions';
import { useToast } from '@/hooks/use-toast';
import { useItems } from '@/context/ItemsContext';
import { useRouter } from 'next/navigation';

const reportItemSchema = z.object({
  name: z.string().min(3, 'Item name must be at least 3 characters.'),
  location: z.string().min(1, 'Please select a location.'),
  description: z.string().min(10, 'Description must be at least 10 characters.'),
  image: z.any().refine(file => file instanceof File, 'Image is required.'),
});

type ReportItemFormValues = z.infer<typeof reportItemSchema>;

export default function ReportItemForm() {
  const [imagePreview, setImagePreview] = useState<string | null>(null);
  const [isAnalyzing, startTransition] = useTransition();
  const { toast } = useToast();
  const { addItem } = useItems();
  const router = useRouter();

  const form = useForm<ReportItemFormValues>({
    resolver: zodResolver(reportItemSchema),
    defaultValues: {
      name: '',
      location: '',
      description: '',
    },
  });

  const handleImageChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    const file = event.target.files?.[0];
    if (file) {
      form.setValue('image', file);
      const reader = new FileReader();
      reader.onloadend = () => {
        const dataUrl = reader.result as string;
        setImagePreview(dataUrl);

        startTransition(async () => {
          const result = await getImageSuggestions({ photoDataUri: dataUrl });
          if (result.success && result.suggestions) {
            const currentDesc = form.getValues('description');
            form.setValue('description', currentDesc ? `${currentDesc}, ${result.suggestions}`: result.suggestions);
            toast({
              title: 'AI Suggestions Added!',
              description: 'We\'ve added some suggested characteristics to your description.',
            });
          } else {
             toast({
              variant: 'destructive',
              title: 'AI Analysis Failed',
              description: result.error || 'Could not get suggestions for the image.',
            });
          }
        });
      };
      reader.readAsDataURL(file);
    }
  };

  function onSubmit(data: ReportItemFormValues) {
    const newItem = {
        id: new Date().getTime().toString(),
        name: data.name,
        description: data.description,
        location: data.location,
        imageUrl: imagePreview!,
        imageHint: '',
        dateFound: new Date().toISOString().split('T')[0],
        status: 'available' as const,
    };
    addItem(newItem);
    
    toast({
      title: "Item Reported!",
      description: "Thank you! Your found item has been successfully reported.",
    });
    form.reset();
    setImagePreview(null);
    router.push('/');
  }

  return (
    <Card>
      <CardContent className="p-6">
        <Form {...form}>
          <form onSubmit={form.handleSubmit(onSubmit)} className="space-y-8">
            <FormField
              control={form.control}
              name="image"
              render={({ field }) => (
                <FormItem>
                  <FormLabel>Item Image</FormLabel>
                  <FormControl>
                    <div className="space-y-4">
                      <Input
                        type="file"
                        accept="image/*"
                        onChange={handleImageChange}
                        className="file:text-primary file:font-semibold"
                      />
                       {imagePreview && (
                        <div className="relative w-full h-64 rounded-md overflow-hidden border">
                          <Image
                            src={imagePreview}
                            alt="Preview of uploaded item"
                            fill
                            className="object-contain"
                          />
                        </div>
                      )}
                      {!imagePreview && (
                        <div className="w-full h-64 rounded-md border-2 border-dashed flex flex-col items-center justify-center bg-muted/50">
                           <ImageIcon className="h-16 w-16 text-muted-foreground" />
                           <p className="mt-2 text-sm text-muted-foreground">Upload an image of the item</p>
                        </div>
                      )}
                    </div>
                  </FormControl>
                  <FormDescription>A clear image helps a lot!</FormDescription>
                  <FormMessage />
                </FormItem>
              )}
            />
            
            <FormField
              control={form.control}
              name="name"
              render={({ field }) => (
                <FormItem>
                  <FormLabel>Item Name</FormLabel>
                  <FormControl>
                    <Input placeholder="e.g., Black Leather Wallet" {...field} />
                  </FormControl>
                  <FormDescription>
                    A brief, descriptive title for the item.
                  </FormDescription>
                  <FormMessage />
                </FormItem>
              )}
            />

            <FormField
              control={form.control}
              name="location"
              render={({ field }) => (
                <FormItem>
                  <FormLabel>Location Found</FormLabel>
                  <FormControl>
                    <Input placeholder="e.g., Library" {...field} />
                  </FormControl>
                   <FormDescription>
                    Where did you find this item?
                  </FormDescription>
                  <FormMessage />
                </FormItem>
              )}
            />

            <FormField
              control={form.control}
              name="description"
              render={({ field }) => (
                <FormItem>
                  <FormLabel>
                    <div className="flex items-center gap-2">
                      Description
                      {isAnalyzing && <Loader2 className="h-4 w-4 animate-spin" />}
                    </div>
                  </FormLabel>
                  <FormControl>
                    <Textarea
                      placeholder="Describe the item, including any identifying marks, color, material, brand, etc."
                      className="min-h-[120px]"
                      {...field}
                    />
                  </FormControl>
                   <FormDescription className="flex items-center gap-1.5">
                    <Sparkles className="h-3.5 w-3.5 text-accent" /> Our AI will help suggest characteristics after you upload an image.
                  </FormDescription>
                  <FormMessage />
                </FormItem>
              )}
            />

            <Button type="submit" className="w-full" disabled={isAnalyzing}>
              {isAnalyzing ? <Loader2 className="mr-2 h-4 w-4 animate-spin" /> : null}
              {isAnalyzing ? 'Analyzing Image...' : 'Submit Report'}
            </Button>
          </form>
        </Form>
      </CardContent>
    </Card>
  );
}
