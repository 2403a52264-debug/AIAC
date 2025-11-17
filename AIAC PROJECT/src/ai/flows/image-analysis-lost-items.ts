// This file is used to analyze images of lost items and suggest relevant characteristics.

'use server';

import {ai} from '@/ai/genkit';
import {z} from 'genkit';

/**
 * @fileOverview An image analysis AI agent for lost items.
 *
 * - analyzeImage - A function that handles the image analysis process.
 * - ImageAnalysisInput - The input type for the analyzeImage function.
 * - ImageAnalysisOutput - The return type for the analyzeImage function.
 */

const ImageAnalysisInputSchema = z.object({
  photoDataUri: z
    .string()
    .describe(
      "A photo of a lost item, as a data URI that must include a MIME type and use Base64 encoding. Expected format: 'data:<mimetype>;base64,<encoded_data>'."
    ),
});
export type ImageAnalysisInput = z.infer<typeof ImageAnalysisInputSchema>;

const ImageAnalysisOutputSchema = z.object({
  suggestedCharacteristics: z
    .string()
    .describe(
      'A list of suggested characteristics for the item, such as color, material, brand, and any other identifiable features.'
    ),
});
export type ImageAnalysisOutput = z.infer<typeof ImageAnalysisOutputSchema>;

export async function analyzeImage(input: ImageAnalysisInput): Promise<ImageAnalysisOutput> {
  return analyzeImageFlow(input);
}

const prompt = ai.definePrompt({
  name: 'imageAnalysisPrompt',
  input: {schema: ImageAnalysisInputSchema},
  output: {schema: ImageAnalysisOutputSchema},
  prompt: `You are an AI assistant designed to analyze images of lost items and suggest relevant characteristics for their description.

  Based on the image, suggest characteristics such as color, material, brand, and any other identifiable features that would help identify the item.
  Make your response concise and comma separated.

  Image: {{media url=photoDataUri}}`,
});

const analyzeImageFlow = ai.defineFlow(
  {
    name: 'analyzeImageFlow',
    inputSchema: ImageAnalysisInputSchema,
    outputSchema: ImageAnalysisOutputSchema,
  },
  async input => {
    const {output} = await prompt(input);
    return output!;
  }
);
