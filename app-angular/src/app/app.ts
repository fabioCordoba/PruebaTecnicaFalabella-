import { Component, inject, signal } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { FormBuilder, FormsModule } from '@angular/forms';
import { AppService } from './service/app.service';
import { HttpClientModule } from '@angular/common/http';
import { DocuemntType, Purchase } from '../interfaces/app.interfaces';
import { JsonPipe, NgFor, NgIf } from '@angular/common';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, FormsModule, HttpClientModule, NgFor, NgIf, JsonPipe],
  templateUrl: './app.html',
  styleUrl: './app.css',
})
export class App {
  protected readonly title = signal('Consulta de Compras');
  private appService = inject(AppService);

  public documentType: DocuemntType[] = [];
  public responseData: Purchase[] = [];

  readonly selectedType = signal<string>('');
  readonly documentNumber = signal<string>('');
  readonly searchResult = signal<string | null>(null);

  private fb = inject(FormBuilder);

  constructor() {
    this.loadDocumentTypes();
  }

  private loadDocumentTypes() {
    this.appService.getDocumentType().subscribe((types) => {
      this.documentType = types;
      console.log(this.documentType);
    });
  }

  search() {
    const type = this.selectedType();
    const number = this.documentNumber();

    console.log(type, number);

    if (!type || !number) {
      this.searchResult.set('⚠️ Por favor completa ambos campos.');
      return;
    }

    this.appService.getPurchasesByDocument(type, number).subscribe((data) => {
      this.searchResult.set(JSON.stringify(data, null, 2));
      // this.responseData = data;
    });

    this.searchResult.set(`🔍 Buscando compras del usuario con ${type} N° ${number}...`);
  }
}
