
'use client';

import React, { createContext, useContext, useState, ReactNode } from 'react';
import type { Item } from '@/lib/definitions';
import { items as initialItems } from '@/lib/data';

interface ItemsContextType {
  items: Item[];
  addItem: (item: Item) => void;
  updateItem: (item: Item) => void;
  deleteItem: (itemId: string) => void;
}

const ItemsContext = createContext<ItemsContextType | undefined>(undefined);

export const ItemsProvider = ({ children }: { children: ReactNode }) => {
  const [items, setItems] = useState<Item[]>(initialItems);

  const addItem = (item: Item) => {
    setItems((prevItems) => [item, ...prevItems]);
  };

  const updateItem = (updatedItem: Item) => {
    setItems((prevItems) =>
      prevItems.map((item) => (item.id === updatedItem.id ? updatedItem : item))
    );
  };

  const deleteItem = (itemId: string) => {
    setItems((prevItems) => prevItems.filter((item) => item.id !== itemId));
  };

  return (
    <ItemsContext.Provider value={{ items, addItem, updateItem, deleteItem }}>
      {children}
    </ItemsContext.Provider>
  );
};

export const useItems = () => {
  const context = useContext(ItemsContext);
  if (context === undefined) {
    throw new Error('useItems must be used within an ItemsProvider');
  }
  return context;
};
