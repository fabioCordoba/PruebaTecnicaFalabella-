export interface DocuemntType {
  id: string;
  name: string;
  short_name: string;
}

export interface Purchase {
  code: string;
  total: string;
  created_at: Date;
  products: Product[];
}

export interface Product {
  product_name: string;
  product_price: string;
  quantity: number;
}
