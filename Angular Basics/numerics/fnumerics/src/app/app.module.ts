import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';

import { NumericsModule } from './modules/numerics/numerics.module';

@NgModule({
  declarations: [
    AppComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    NumericsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
