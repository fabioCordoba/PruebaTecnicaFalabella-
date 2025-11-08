import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { environment } from '../../environments/environments';
import { catchError, Observable, throwError } from 'rxjs';
import { DocuemntType, Purchase } from '../../interfaces/app.interfaces';

@Injectable({
  providedIn: 'root',
})
export class AppService {
  private readonly baseUrl = environment.baseUrl;

  constructor(private http: HttpClient) {}

  /** 🔹 Obtener tipos de documento */
  getDocumentType(): Observable<DocuemntType[]> {
    const url = `${this.baseUrl}/api/docment_type/`; // 👈 corregido

    return this.http.get<DocuemntType[]>(url).pipe(
      catchError((error) => {
        console.error('Error al obtener tipos de documento:', error);
        return throwError(() => new Error(error.message || 'Error en la solicitud'));
      })
    );
  }

  /** 🔹 Buscar compras por tipo y número de documento */
  getPurchasesByDocument(type: string, document: string): Observable<Purchase[]> {
    console.log(type, document);

    const url = `${this.baseUrl}/api/purchases/${document}/`;
    return this.http.get<Purchase[]>(url, { params: { type, document } }).pipe(
      catchError((error) => {
        console.error('Error al buscar compras:', error);
        return throwError(() => new Error(error.message || 'Error al buscar compras'));
      })
    );
  }

  /** 🔹 Buscar compras por tipo y número de documento y exportar excel*/
  exportPurchasesByDocument(type: string, document: string): Observable<Blob> {
    console.log(type, document);

    const url = `${this.baseUrl}/api/export-excel/`;
    const params = {
      document_type: type,
      document_number: document,
    };

    return this.http
      .get(url, {
        params,
        responseType: 'blob',
      })
      .pipe(
        catchError((error) => {
          console.error('Error al exportar compras:', error);
          return throwError(() => new Error(error.message || 'Error al exportar compras'));
        })
      );
  }
}
