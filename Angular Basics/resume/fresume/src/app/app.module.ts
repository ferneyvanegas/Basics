import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';

// Módulos
import { LandingModule } from './modules/landing/landing.module';
import { FontAwesomeModule } from '@fortawesome/angular-fontawesome';

// Componentes
import { NavBarComponent } from './modules/template/nav-bar/nav-bar.component';
import { FooterComponent } from './modules/template/footer/footer.component';
 
@NgModule({
  declarations: [
    AppComponent,
    NavBarComponent,
    FooterComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    LandingModule,
    FontAwesomeModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
