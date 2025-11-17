"use server";

import {
  analyzeImage as analyzeImageFlow,
  type ImageAnalysisInput,
} from '@/ai/flows/image-analysis-lost-items';

export async function getImageSuggestions(data: ImageAnalysisInput) {
  try {
    const result = await analyzeImageFlow(data);
    return { success: true, suggestions: result.suggestedCharacteristics };
  } catch (error) {
    console.error(error);
    return { success: false, error: "Failed to analyze image." };
  }
}
