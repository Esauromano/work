<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>ARMSApp</class>
 <widget class="QMainWindow" name="ARMSApp">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>1835</width>
    <height>1153</height>
   </rect>
  </property>
  <property name="palette">
   <palette>
    <active>
     <colorrole role="Button">
      <brush brushstyle="SolidPattern">
       <color alpha="255">
        <red>0</red>
        <green>0</green>
        <blue>0</blue>
       </color>
      </brush>
     </colorrole>
     <colorrole role="Base">
      <brush brushstyle="SolidPattern">
       <color alpha="255">
        <red>0</red>
        <green>0</green>
        <blue>0</blue>
       </color>
      </brush>
     </colorrole>
     <colorrole role="Window">
      <brush brushstyle="SolidPattern">
       <color alpha="255">
        <red>0</red>
        <green>0</green>
        <blue>0</blue>
       </color>
      </brush>
     </colorrole>
    </active>
    <inactive>
     <colorrole role="Button">
      <brush brushstyle="SolidPattern">
       <color alpha="255">
        <red>0</red>
        <green>0</green>
        <blue>0</blue>
       </color>
      </brush>
     </colorrole>
     <colorrole role="Base">
      <brush brushstyle="SolidPattern">
       <color alpha="255">
        <red>0</red>
        <green>0</green>
        <blue>0</blue>
       </color>
      </brush>
     </colorrole>
     <colorrole role="Window">
      <brush brushstyle="SolidPattern">
       <color alpha="255">
        <red>0</red>
        <green>0</green>
        <blue>0</blue>
       </color>
      </brush>
     </colorrole>
    </inactive>
    <disabled>
     <colorrole role="Button">
      <brush brushstyle="SolidPattern">
       <color alpha="255">
        <red>0</red>
        <green>0</green>
        <blue>0</blue>
       </color>
      </brush>
     </colorrole>
     <colorrole role="Base">
      <brush brushstyle="SolidPattern">
       <color alpha="255">
        <red>0</red>
        <green>0</green>
        <blue>0</blue>
       </color>
      </brush>
     </colorrole>
     <colorrole role="Window">
      <brush brushstyle="SolidPattern">
       <color alpha="255">
        <red>0</red>
        <green>0</green>
        <blue>0</blue>
       </color>
      </brush>
     </colorrole>
    </disabled>
   </palette>
  </property>
  <property name="windowTitle">
   <string>ARMSApp</string>
  </property>
  <property name="windowIcon">
   <iconset resource="recursos.qrc">
    <normaloff>:/Img/arms_icon.png</normaloff>:/Img/arms_icon.png</iconset>
  </property>
  <property name="autoFillBackground">
   <bool>false</bool>
  </property>
  <property name="styleSheet">
   <string notr="true">QMainWindow#ARMSApp
{
border-image: url(:/Img/arms_fondo.png) 0 0 0 0 stretch stretch;
background: url(:/Img/arms_fondo.png) no-repeat center center fixed
}</string>
  </property>
  <property name="tabShape">
   <enum>QTabWidget::Triangular</enum>
  </property>
  <widget class="QWidget" name="centralWidget">
   <layout class="QGridLayout" name="gridLayout_29">
    <item row="0" column="0">
     <widget class="QFrame" name="frame">
      <property name="frameShape">
       <enum>QFrame::NoFrame</enum>
      </property>
      <property name="frameShadow">
       <enum>QFrame::Raised</enum>
      </property>
      <layout class="QGridLayout" name="gridLayout_34">
       <item row="0" column="0">
        <widget class="QTabWidget" name="tabWidget">
         <property name="palette">
          <palette>
           <active/>
           <inactive/>
           <disabled/>
          </palette>
         </property>
         <property name="layoutDirection">
          <enum>Qt::LeftToRight</enum>
         </property>
         <property name="styleSheet">
          <string notr="true">QTabBar::tab
{
border: 0px solid white;
background-color: rgb(41,180,115);
border-radius: 1px;
font: bold 14px;
padding: 5px;
color: rgb(255,255,255);
margin: 2px;
width: 30px;
height: 150px;
} 

QTabBar::tab::selected
{
background-color:  rgb(24,158,87);
} 

QTabBar::tab:hover
{
font:  14px;
}
</string>
         </property>
         <property name="tabPosition">
          <enum>QTabWidget::West</enum>
         </property>
         <property name="currentIndex">
          <number>1</number>
         </property>
         <property name="elideMode">
          <enum>Qt::ElideRight</enum>
         </property>
         <property name="usesScrollButtons">
          <bool>false</bool>
         </property>
         <widget class="QWidget" name="widget">
          <attribute name="title">
           <string>Iniciar sesión</string>
          </attribute>
          <layout class="QVBoxLayout" name="verticalLayout_2">
           <item>
            <widget class="QTabWidget" name="tabWidget_2">
             <property name="styleSheet">
              <string notr="true">QTabBar::tab
{
border: 0px solid white;
background-color: rgb(41,180,115);
border-radius: 1px;
font: bold 14px;
padding: 5px;
color: rgb(255,255,255);
margin: 2px;
width: 150px;
height: 30px;
} 

QTabBar::tab::selected
{
background-color:  rgb(24,158,87);
} 

QTabBar::tab:hover
{
font:  14px;
}
</string>
             </property>
             <property name="currentIndex">
              <number>0</number>
             </property>
             <widget class="QWidget" name="tab">
              <attribute name="title">
               <string>Acceso</string>
              </attribute>
              <layout class="QGridLayout" name="gridLayout_26">
               <item row="0" column="1">
                <spacer name="verticalSpacer_2">
                 <property name="orientation">
                  <enum>Qt::Vertical</enum>
                 </property>
                 <property name="sizeHint" stdset="0">
                  <size>
                   <width>20</width>
                   <height>13</height>
                  </size>
                 </property>
                </spacer>
               </item>
               <item row="1" column="0">
                <spacer name="horizontalSpacer">
                 <property name="orientation">
                  <enum>Qt::Horizontal</enum>
                 </property>
                 <property name="sizeHint" stdset="0">
                  <size>
                   <width>360</width>
                   <height>20</height>
                  </size>
                 </property>
                </spacer>
               </item>
               <item row="1" column="1" colspan="2">
                <widget class="QGroupBox" name="groupBox_2">
                 <property name="styleSheet">
                  <string notr="true">background-color: rgb(230,231,232);
margin-top: 0.5em;
font: 16px;
color:  rgb(97,98,97);
border: 0px solid white;
padding: 14;
</string>
                 </property>
                 <property name="title">
                  <string/>
                 </property>
                 <layout class="QGridLayout" name="gridLayout_22">
                  <item row="1" column="0">
                   <widget class="QFrame" name="frame_45">
                    <property name="minimumSize">
                     <size>
                      <width>300</width>
                      <height>300</height>
                     </size>
                    </property>
                    <property name="maximumSize">
                     <size>
                      <width>500</width>
                      <height>500</height>
                     </size>
                    </property>
                    <property name="styleSheet">
                     <string notr="true">font: 11px;
color: rgb(160, 232, 105);
border: 0px solid rgba(143, 234, 79,90);
background-color: rgba(0,0,0,0);
</string>
                    </property>
                    <property name="frameShape">
                     <enum>QFrame::NoFrame</enum>
                    </property>
                    <property name="frameShadow">
                     <enum>QFrame::Raised</enum>
                    </property>
                    <layout class="QGridLayout" name="gridLayout_57">
                     <item row="1" column="0">
                      <spacer name="horizontalSpacer_15">
                       <property name="orientation">
                        <enum>Qt::Horizontal</enum>
                       </property>
                       <property name="sizeHint" stdset="0">
                        <size>
                         <width>88</width>
                         <height>20</height>
                        </size>
                       </property>
                      </spacer>
                     </item>
                     <item row="3" column="2">
                      <widget class="QLineEdit" name="lineEditClave_2">
                       <property name="styleSheet">
                        <string notr="true">background-color: rgb(255,255,255);

font: 16px;
color: rgb(97,98,97);
border-color: rgb(26,154,198);

border: 0px solid white;
border-radius: 0px;
padding: 2px;
margin-top: 0.01em;
</string>
                       </property>
                       <property name="echoMode">
                        <enum>QLineEdit::Password</enum>
                       </property>
                       <property name="placeholderText">
                        <string>Clave</string>
                       </property>
                      </widget>
                     </item>
                     <item row="0" column="2">
                      <spacer name="verticalSpacer_12">
                       <property name="orientation">
                        <enum>Qt::Vertical</enum>
                       </property>
                       <property name="sizeHint" stdset="0">
                        <size>
                         <width>20</width>
                         <height>55</height>
                        </size>
                       </property>
                      </spacer>
                     </item>
                     <item row="2" column="2">
                      <widget class="QLineEdit" name="lineEditUsuario_2">
                       <property name="styleSheet">
                        <string notr="true">background-color: rgb(255,255,255);

font: 16px;
color: rgb(97,98,97);
border-color: rgb(26,154,198);

border: 0px solid white;
border-radius: 0px;
padding: 2px;
margin-top: 0.01em;
</string>
                       </property>
                       <property name="placeholderText">
                        <string>Usuario</string>
                       </property>
                      </widget>
                     </item>
                     <item row="5" column="2">
                      <spacer name="verticalSpacer_13">
                       <property name="orientation">
                        <enum>Qt::Vertical</enum>
                       </property>
                       <property name="sizeHint" stdset="0">
                        <size>
                         <width>20</width>
                         <height>55</height>
                        </size>
                       </property>
                      </spacer>
                     </item>
                     <item row="1" column="3">
                      <spacer name="horizontalSpacer_18">
                       <property name="orientation">
                        <enum>Qt::Horizontal</enum>
                       </property>
                       <property name="sizeHint" stdset="0">
                        <size>
                         <width>40</width>
                         <height>20</height>
                        </size>
                       </property>
                      </spacer>
                     </item>
                     <item row="1" column="2">
                      <widget class="QLineEdit" name="lineEditCEDI_2">
                       <property name="minimumSize">
                        <size>
                         <width>250</width>
                         <height>0</height>
                        </size>
                       </property>
                       <property name="styleSheet">
                        <string notr="true">background-color: rgb(255,255,255);

font: 16px;
color: rgb(97,98,97);
border-color: rgb(26,154,198);

border: 0px solid white;
border-radius: 0px;
padding: 2px;
margin-top: 0.01em;
</string>
                       </property>
                       <property name="text">
                        <string>CENADI</string>
                       </property>
                       <property name="placeholderText">
                        <string>CEDI</string>
                       </property>
                      </widget>
                     </item>
                     <item row="4" column="2">
                      <widget class="QPushButton" name="pushButtonIniciaSesion_2">
                       <property name="palette">
                        <palette>
                         <active>
                          <colorrole role="WindowText">
                           <brush brushstyle="SolidPattern">
                            <color alpha="255">
                             <red>255</red>
                             <green>255</green>
                             <blue>255</blue>
                            </color>
                           </brush>
                          </colorrole>
                          <colorrole role="Button">
                           <brush brushstyle="SolidPattern">
                            <color alpha="255">
                             <red>24</red>
                             <green>158</green>
                             <blue>87</blue>
                            </color>
                           </brush>
                          </colorrole>
                          <colorrole role="Text">
                           <brush brushstyle="SolidPattern">
                            <color alpha="255">
                             <red>255</red>
                             <green>255</green>
                             <blue>255</blue>
                            </color>
                           </brush>
                          </colorrole>
                          <colorrole role="ButtonText">
                           <brush brushstyle="SolidPattern">
                            <color alpha="255">
                             <red>255</red>
                             <green>255</green>
                             <blue>255</blue>
                            </color>
                           </brush>
                          </colorrole>
                          <colorrole role="Base">
                           <brush brushstyle="SolidPattern">
                            <color alpha="255">
                             <red>24</red>
                             <green>158</green>
                             <blue>87</blue>
                            </color>
                           </brush>
                          </colorrole>
                          <colorrole role="Window">
                           <brush brushstyle="SolidPattern">
                            <color alpha="255">
                             <red>24</red>
                             <green>158</green>
                             <blue>87</blue>
                            </color>
                           </brush>
                          </colorrole>
                         </active>
                         <inactive>
                          <colorrole role="WindowText">
                           <brush brushstyle="SolidPattern">
                            <color alpha="255">
                             <red>255</red>
                             <green>255</green>
                             <blue>255</blue>
                            </color>
                           </brush>
                          </colorrole>
                          <colorrole role="Button">
                           <brush brushstyle="SolidPattern">
                            <color alpha="255">
                             <red>24</red>
                             <green>158</green>
                             <blue>87</blue>
                            </color>
                           </brush>
                          </colorrole>
                          <colorrole role="Text">
                           <brush brushstyle="SolidPattern">
                            <color alpha="255">
                             <red>255</red>
                             <green>255</green>
                             <blue>255</blue>
                            </color>
                           </brush>
                          </colorrole>
                          <colorrole role="ButtonText">
                           <brush brushstyle="SolidPattern">
                            <color alpha="255">
                             <red>255</red>
                             <green>255</green>
                             <blue>255</blue>
                            </color>
                           </brush>
                          </colorrole>
                          <colorrole role="Base">
                           <brush brushstyle="SolidPattern">
                            <color alpha="255">
                             <red>24</red>
                             <green>158</green>
                             <blue>87</blue>
                            </color>
                           </brush>
                          </colorrole>
                          <colorrole role="Window">
                           <brush brushstyle="SolidPattern">
                            <color alpha="255">
                             <red>24</red>
                             <green>158</green>
                             <blue>87</blue>
                            </color>
                           </brush>
                          </colorrole>
                         </inactive>
                         <disabled>
                          <colorrole role="WindowText">
                           <brush brushstyle="SolidPattern">
                            <color alpha="255">
                             <red>255</red>
                             <green>255</green>
                             <blue>255</blue>
                            </color>
                           </brush>
                          </colorrole>
                          <colorrole role="Button">
                           <brush brushstyle="SolidPattern">
                            <color alpha="255">
                             <red>24</red>
                             <green>158</green>
                             <blue>87</blue>
                            </color>
                           </brush>
                          </colorrole>
                          <colorrole role="Text">
                           <brush brushstyle="SolidPattern">
                            <color alpha="255">
                             <red>255</red>
                             <green>255</green>
                             <blue>255</blue>
                            </color>
                           </brush>
                          </colorrole>
                          <colorrole role="ButtonText">
                           <brush brushstyle="SolidPattern">
                            <color alpha="255">
                             <red>255</red>
                             <green>255</green>
                             <blue>255</blue>
                            </color>
                           </brush>
                          </colorrole>
                          <colorrole role="Base">
                           <brush brushstyle="SolidPattern">
                            <color alpha="255">
                             <red>24</red>
                             <green>158</green>
                             <blue>87</blue>
                            </color>
                           </brush>
                          </colorrole>
                          <colorrole role="Window">
                           <brush brushstyle="SolidPattern">
                            <color alpha="255">
                             <red>24</red>
                             <green>158</green>
                             <blue>87</blue>
                            </color>
                           </brush>
                          </colorrole>
                         </disabled>
                        </palette>
                       </property>
                       <property name="styleSheet">
                        <string notr="true">QPushButton
{
background-color: rgb(24,158,87);
border-radius: 5px;
font: bold 14px;
padding: 5px;
color: rgb(255,255,255);
} </string>
                       </property>
                       <property name="text">
                        <string>Iniciar</string>
                       </property>
                      </widget>
                     </item>
                    </layout>
                   </widget>
                  </item>
                  <item row="0" column="0">
                   <widget class="QLabel" name="labelStatusBarCEDI_7">
                    <property name="maximumSize">
                     <size>
                      <width>500</width>
                      <height>175</height>
                     </size>
                    </property>
                    <property name="styleSheet">
                     <string notr="true">background-color: rgba(0,0,0,0);
</string>
                    </property>
                    <property name="text">
                     <string/>
                    </property>
                    <property name="pixmap">
                     <pixmap resource="recursos.qrc">:/Img/arete_group.png</pixmap>
                    </property>
                    <property name="scaledContents">
                     <bool>false</bool>
                    </property>
                    <property name="alignment">
                     <set>Qt::AlignCenter</set>
                    </property>
                   </widget>
                  </item>
                 </layout>
                </widget>
               </item>
               <item row="1" column="3">
                <spacer name="horizontalSpacer_3">
                 <property name="orientation">
                  <enum>Qt::Horizontal</enum>
                 </property>
                 <property name="sizeHint" stdset="0">
                  <size>
                   <width>360</width>
                   <height>20</height>
                  </size>
                 </property>
                </spacer>
               </item>
               <item row="2" column="2">
                <spacer name="verticalSpacer_3">
                 <property name="orientation">
                  <enum>Qt::Vertical</enum>
                 </property>
                 <property name="sizeHint" stdset="0">
                  <size>
                   <width>20</width>
                   <height>13</height>
                  </size>
                 </property>
                </spacer>
               </item>
              </layout>
             </widget>
             <widget class="QWidget" name="tab_2">
              <attribute name="title">
               <string>Acerca de ARMS...</string>
              </attribute>
              <layout class="QGridLayout" name="gridLayout_47">
               <item row="0" column="0">
                <widget class="QGroupBox" name="groupBox_3">
                 <property name="styleSheet">
                  <string notr="true">background-color: rgba(255,255,255,50);
margin-top: 0.5em;
font: bold 18px;
color: rgb(102,102,102);
border: 0px solid white;
padding: 13px;
</string>
                 </property>
                 <property name="title">
                  <string/>
                 </property>
                 <layout class="QGridLayout" name="gridLayout_64">
                  <item row="0" column="0">
                   <widget class="QTextEdit" name="textEdit">
                    <property name="styleSheet">
                     <string notr="true">background-color: rgb(230,231,232);
margin-top: 0.5em;
font: 16px;
color:  rgb(97,98,97);
border: 0px solid white;
padding: 14;
</string>
                    </property>
                    <property name="html">
                     <string>&lt;!DOCTYPE HTML PUBLIC &quot;-//W3C//DTD HTML 4.0//EN&quot; &quot;http://www.w3.org/TR/REC-html40/strict.dtd&quot;&gt;
&lt;html&gt;&lt;head&gt;&lt;meta name=&quot;qrichtext&quot; content=&quot;1&quot; /&gt;&lt;style type=&quot;text/css&quot;&gt;
p, li { white-space: pre-wrap; }
&lt;/style&gt;&lt;/head&gt;&lt;body style=&quot; font-family:'.SF NS Text'; font-size:16px; font-weight:400; font-style:normal;&quot;&gt;
&lt;p align=&quot;center&quot; style=&quot;-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;&lt;br /&gt;&lt;/p&gt;
&lt;p align=&quot;center&quot; style=&quot;-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:64pt;&quot;&gt;&lt;br /&gt;&lt;/p&gt;
&lt;p align=&quot;center&quot; style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;&lt;span style=&quot; font-size:64pt;&quot;&gt;ARMS 3.5&lt;/span&gt;&lt;/p&gt;
&lt;p align=&quot;center&quot; style=&quot;-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:64pt;&quot;&gt;&lt;br /&gt;&lt;/p&gt;
&lt;p align=&quot;center&quot; style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;&lt;span style=&quot; font-size:18px;&quot;&gt;Release 3.5.0.0.12&lt;/span&gt;&lt;/p&gt;
&lt;p align=&quot;center&quot; style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;&lt;span style=&quot; font-size:18px;&quot;&gt;12 nov 2017&lt;/span&gt;&lt;/p&gt;
&lt;p align=&quot;center&quot; style=&quot;-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18px;&quot;&gt;&lt;br /&gt;&lt;/p&gt;
&lt;p align=&quot;center&quot; style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;&lt;span style=&quot; font-size:18px;&quot;&gt;Grupo Areté&lt;/span&gt;&lt;/p&gt;
&lt;p align=&quot;center&quot; style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;&lt;span style=&quot; font-size:18px;&quot;&gt;Derechos Reservados&lt;/span&gt;&lt;/p&gt;
&lt;p align=&quot;center&quot; style=&quot;-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18px;&quot;&gt;&lt;br /&gt;&lt;/p&gt;
&lt;p align=&quot;center&quot; style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;&lt;span style=&quot; font-size:18px;&quot;&gt;www.arete.ws&lt;/span&gt;&lt;/p&gt;
&lt;p style=&quot;-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18px; font-weight:600;&quot;&gt;&lt;br /&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
                    </property>
                   </widget>
                  </item>
                 </layout>
                </widget>
               </item>
               <item row="1" column="0">
                <widget class="QFrame" name="frame_43">
                 <property name="styleSheet">
                  <string notr="true">border-radius: 0px;</string>
                 </property>
                 <property name="frameShape">
                  <enum>QFrame::StyledPanel</enum>
                 </property>
                 <property name="frameShadow">
                  <enum>QFrame::Raised</enum>
                 </property>
                 <layout class="QGridLayout" name="gridLayout_23">
                  <item row="4" column="0">
                   <widget class="QLabel" name="labelStatusBarUser">
                    <property name="text">
                     <string>user</string>
                    </property>
                   </widget>
                  </item>
                  <item row="5" column="0">
                   <widget class="QProgressBar" name="progressBarStatus">
                    <property name="value">
                     <number>24</number>
                    </property>
                   </widget>
                  </item>
                  <item row="0" column="0">
                   <widget class="QLabel" name="labelStatusBarCEDI">
                    <property name="text">
                     <string>CEDI</string>
                    </property>
                   </widget>
                  </item>
                  <item row="3" column="0">
                   <widget class="QLabel" name="labelStatusBarMensaje">
                    <property name="text">
                     <string>Mensaje</string>
                    </property>
                   </widget>
                  </item>
                  <item row="2" column="0">
                   <widget class="QLabel" name="labelStatusBarEmpresa">
                    <property name="text">
                     <string>empresa</string>
                    </property>
                   </widget>
                  </item>
                 </layout>
                </widget>
               </item>
              </layout>
             </widget>
            </widget>
           </item>
           <item>
            <widget class="QLabel" name="labelStatusBarCEDI_2">
             <property name="text">
              <string/>
             </property>
             <property name="pixmap">
              <pixmap resource="recursos.qrc">:/Img/arms_logo.png</pixmap>
             </property>
             <property name="alignment">
              <set>Qt::AlignCenter</set>
             </property>
            </widget>
           </item>
          </layout>
         </widget>
         <widget class="QWidget" name="tabInterfase">
          <attribute name="title">
           <string>Interfaz</string>
          </attribute>
          <layout class="QGridLayout" name="gridLayout_55">
           <item row="0" column="0">
            <widget class="QTabWidget" name="tabWidget_7">
             <property name="styleSheet">
              <string notr="true">QTabBar::tab
{
border: 0px solid white;
background-color: rgb(41,180,115);
border-radius: 1px;
font: bold 14px;
padding: 5px;
color: rgb(255,255,255);
margin: 2px;
width: 250px;
height: 30px;
} 

QTabBar::tab::selected
{
background-color:  rgb(24,158,87);
} 

QTabBar::tab:hover
{
font:  14px;
}
</string>
             </property>
             <property name="tabPosition">
              <enum>QTabWidget::North</enum>
             </property>
             <property name="currentIndex">
              <number>0</number>
             </property>
             <widget class="QWidget" name="tab_5">
              <attribute name="title">
               <string>Pochteca</string>
              </attribute>
              <layout class="QGridLayout" name="gridLayout_9">
               <item row="0" column="0">
                <widget class="QTabWidget" name="tabWidget_3">
                 <property name="currentIndex">
                  <number>0</number>
                 </property>
                 <widget class="QWidget" name="tab_11">
                  <attribute name="title">
                   <string>Pedidos/Operadores</string>
                  </attribute>
                  <layout class="QGridLayout" name="gridLayout_37">
                   <item row="0" column="0">
                    <widget class="QGroupBox" name="groupBox_8">
                     <property name="styleSheet">
                      <string notr="true">background-color: rgb(230,231,232);
margin-top: 0.5em;
font: 16px;
color:  rgb(97,98,97);
border: 0px solid white;
padding: 14;
</string>
                     </property>
                     <property name="title">
                      <string>FTP</string>
                     </property>
                     <layout class="QGridLayout" name="gridLayout_35">
                      <item row="0" column="0">
                       <widget class="QFrame" name="frame_3">
                        <property name="styleSheet">
                         <string notr="true">font: 11px;
color: rgb(97,98,97);
border: 0px solid rgba(143, 234, 79,90);
background-color: rgb(255,255,255);
</string>
                        </property>
                        <property name="frameShape">
                         <enum>QFrame::NoFrame</enum>
                        </property>
                        <property name="frameShadow">
                         <enum>QFrame::Raised</enum>
                        </property>
                        <layout class="QGridLayout" name="gridLayout_10">
                         <item row="0" column="0">
                          <widget class="QRadioButton" name="radioButtonInterfasePochtecaPedidos">
                           <property name="styleSheet">
                            <string notr="true">QRadioButton {
background-color:   rgba(255,0,0,0);
font: 16px;
color:rgb(97,98,97);
padding: 1px;
border: 0px solid rgba(143, 234, 79,90);
}


QRadioButton::indicator:checked {
    background-color:       rgb(41,180,115);
    border:                 0px solid white;
}






</string>
                           </property>
                           <property name="text">
                            <string>Pedidos</string>
                           </property>
                           <property name="checked">
                            <bool>true</bool>
                           </property>
                          </widget>
                         </item>
                         <item row="1" column="0">
                          <widget class="QRadioButton" name="radioButtonInterfasePochtecaOperadores">
                           <property name="styleSheet">
                            <string notr="true">QRadioButton {
background-color:   rgba(255,0,0,0);
font: 16px;
color:rgb(97,98,97);
padding: 1px;
border: 0px solid rgba(143, 234, 79,90);
}


QRadioButton::indicator:checked {
    background-color:       rgb(41,180,115);
    border:                 0px solid white;
}






</string>
                           </property>
                           <property name="text">
                            <string>Operadores</string>
                           </property>
                          </widget>
                         </item>
                         <item row="2" column="0">
                          <widget class="QRadioButton" name="radioButtonInterfasePochtecaDestinos">
                           <property name="styleSheet">
                            <string notr="true">QRadioButton {
background-color:   rgba(255,0,0,0);
font: 16px;
color:rgb(97,98,97);
padding: 1px;
border: 0px solid rgba(143, 234, 79,90);
}


QRadioButton::indicator:checked {
    background-color:       rgb(41,180,115);
    border:                 0px solid white;
}






</string>
                           </property>
                           <property name="text">
                            <string>Destinos</string>
                           </property>
                          </widget>
                         </item>
                        </layout>
                       </widget>
                      </item>
                      <item row="0" column="1" rowspan="2">
                       <widget class="QListWidget" name="listWidgetPochtecaFTP">
                        <property name="styleSheet">
                         <string notr="true">font: 11px;
color: rgb(97,98,97);
border: 0px solid rgba(143, 234, 79,90);
background-color: rgb(255,255,255);
</string>
                        </property>
                        <property name="frameShape">
                         <enum>QFrame::NoFrame</enum>
                        </property>
                        <property name="frameShadow">
                         <enum>QFrame::Plain</enum>
                        </property>
                       </widget>
                      </item>
                      <item row="1" column="0">
                       <widget class="QFrame" name="frame_27">
                        <property name="styleSheet">
                         <string notr="true">font: 11px;
color: rgb(97,98,97);
border: 0px solid rgba(143, 234, 79,90);
background-color: rgb(255,255,255);
</string>
                        </property>
                        <property name="frameShape">
                         <enum>QFrame::NoFrame</enum>
                        </property>
                        <property name="frameShadow">
                         <enum>QFrame::Raised</enum>
                        </property>
                        <layout class="QGridLayout" name="gridLayout_13">
                         <item row="3" column="0">
                          <widget class="QRadioButton" name="radioButtonInterfasePochtecaUrgentes">
                           <property name="styleSheet">
                            <string notr="true">QRadioButton {
background-color:   rgba(255,0,0,0);
font: 16px;
color:rgb(97,98,97);
padding: 1px;
border: 0px solid rgba(143, 234, 79,90);
}


QRadioButton::indicator:checked {
    background-color:       rgb(41,180,115);
    border:                 0px solid white;
}






</string>
                           </property>
                           <property name="text">
                            <string>Urgentes</string>
                           </property>
                           <property name="checked">
                            <bool>false</bool>
                           </property>
                          </widget>
                         </item>
                         <item row="2" column="0">
                          <widget class="QRadioButton" name="radioButtonInterfasePochtecaCancelados">
                           <property name="styleSheet">
                            <string notr="true">QRadioButton {
background-color:   rgba(255,0,0,0);
font: 16px;
color:rgb(97,98,97);
padding: 1px;
border: 0px solid rgba(143, 234, 79,90);
}


QRadioButton::indicator:checked {
    background-color:       rgb(41,180,115);
    border:                 0px solid white;
}






</string>
                           </property>
                           <property name="text">
                            <string>Cancelados</string>
                           </property>
                          </widget>
                         </item>
                         <item row="1" column="0">
                          <widget class="QRadioButton" name="radioButtonInterfasePochtecaOrdinarios">
                           <property name="styleSheet">
                            <string notr="true">QRadioButton {
background-color:   rgba(255,0,0,0);
font: 16px;
color:rgb(97,98,97);
padding: 1px;
border: 0px solid rgba(143, 234, 79,90);
}


QRadioButton::indicator:checked {
    background-color:       rgb(41,180,115);
    border:                 0px solid white;
}






</string>
                           </property>
                           <property name="text">
                            <string>Ordinarios</string>
                           </property>
                          </widget>
                         </item>
                         <item row="0" column="0">
                          <widget class="QRadioButton" name="radioButtonInterfasePochtecaTodos">
                           <property name="styleSheet">
                            <string notr="true">QRadioButton {
background-color:   rgba(255,0,0,0);
font: 16px;
color:rgb(97,98,97);
padding: 1px;
border: 0px solid rgba(143, 234, 79,90);
}


QRadioButton::indicator:checked {
    background-color:       rgb(41,180,115);
    border:                 0px solid white;
}






</string>
                           </property>
                           <property name="text">
                            <string>Todos</string>
                           </property>
                           <property name="checked">
                            <bool>true</bool>
                           </property>
                          </widget>
                         </item>
                         <item row="4" column="0">
                          <spacer name="verticalSpacer_9">
                           <property name="orientation">
                            <enum>Qt::Vertical</enum>
                           </property>
                           <property name="sizeHint" stdset="0">
                            <size>
                             <width>20</width>
                             <height>40</height>
                            </size>
                           </property>
                          </spacer>
                         </item>
                        </layout>
                       </widget>
                      </item>
                      <item row="2" column="1">
                       <widget class="QPushButton" name="pushButtonInterfasePochtecaGenera">
                        <property name="palette">
                         <palette>
                          <active>
                           <colorrole role="WindowText">
                            <brush brushstyle="SolidPattern">
                             <color alpha="255">
                              <red>255</red>
                              <green>255</green>
                              <blue>255</blue>
                             </color>
                            </brush>
                           </colorrole>
                           <colorrole role="Button">
                            <brush brushstyle="SolidPattern">
                             <color alpha="255">
                              <red>24</red>
                              <green>158</green>
                              <blue>87</blue>
                             </color>
                            </brush>
                           </colorrole>
                           <colorrole role="Text">
                            <brush brushstyle="SolidPattern">
                             <color alpha="255">
                              <red>255</red>
                              <green>255</green>
                              <blue>255</blue>
                             </color>
                            </brush>
                           </colorrole>
                           <colorrole role="ButtonText">
                            <brush brushstyle="SolidPattern">
                             <color alpha="255">
                              <red>255</red>
                              <green>255</green>
                              <blue>255</blue>
                             </color>
                            </brush>
                           </colorrole>
                           <colorrole role="Base">
                            <brush brushstyle="SolidPattern">
                             <color alpha="255">
                              <red>24</red>
                              <green>158</green>
                              <blue>87</blue>
                             </color>
                            </brush>
                           </colorrole>
                           <colorrole role="Window">
                            <brush brushstyle="SolidPattern">
                             <color alpha="255">
                              <red>24</red>
                              <green>158</green>
                              <blue>87</blue>
                             </color>
                            </brush>
                           </colorrole>
                          </active>
                          <inactive>
                           <colorrole role="WindowText">
                            <brush brushstyle="SolidPattern">
                             <color alpha="255">
                              <red>255</red>
                              <green>255</green>
                              <blue>255</blue>
                             </color>
                            </brush>
                           </colorrole>
                           <colorrole role="Button">
                            <brush brushstyle="SolidPattern">
                             <color alpha="255">
                              <red>24</red>
                              <green>158</green>
                              <blue>87</blue>
                             </color>
                            </brush>
                           </colorrole>
                           <colorrole role="Text">
                            <brush brushstyle="SolidPattern">
                             <color alpha="255">
                              <red>255</red>
                              <green>255</green>
                              <blue>255</blue>
                             </color>
                            </brush>
                           </colorrole>
                           <colorrole role="ButtonText">
                            <brush brushstyle="SolidPattern">
                             <color alpha="255">
                              <red>255</red>
                              <green>255</green>
                              <blue>255</blue>
                             </color>
                            </brush>
                           </colorrole>
                           <colorrole role="Base">
                            <brush brushstyle="SolidPattern">
                             <color alpha="255">
                              <red>24</red>
                              <green>158</green>
                              <blue>87</blue>
                             </color>
                            </brush>
                           </colorrole>
                           <colorrole role="Window">
                            <brush brushstyle="SolidPattern">
                             <color alpha="255">
                              <red>24</red>
                              <green>158</green>
                              <blue>87</blue>
                             </color>
                            </brush>
                           </colorrole>
                          </inactive>
                          <disabled>
                           <colorrole role="WindowText">
                            <brush brushstyle="SolidPattern">
                             <color alpha="255">
                              <red>255</red>
                              <green>255</green>
                              <blue>255</blue>
                             </color>
                            </brush>
                           </colorrole>
                           <colorrole role="Button">
                            <brush brushstyle="SolidPattern">
                             <color alpha="255">
                              <red>24</red>
                              <green>158</green>
                              <blue>87</blue>
                             </color>
                            </brush>
                           </colorrole>
                           <colorrole role="Text">
                            <brush brushstyle="SolidPattern">
                             <color alpha="255">
                              <red>255</red>
                              <green>255</green>
                              <blue>255</blue>
                             </color>
                            </brush>
                           </colorrole>
                           <colorrole role="ButtonText">
                            <brush brushstyle="SolidPattern">
                             <color alpha="255">
                              <red>255</red>
                              <green>255</green>
                              <blue>255</blue>
                             </color>
                            </brush>
                           </colorrole>
                           <colorrole role="Base">
                            <brush brushstyle="SolidPattern">
                             <color alpha="255">
                              <red>24</red>
                              <green>158</green>
                              <blue>87</blue>
                             </color>
                            </brush>
                           </colorrole>
                           <colorrole role="Window">
                            <brush brushstyle="SolidPattern">
                             <color alpha="255">
                              <red>24</red>
                              <green>158</green>
                              <blue>87</blue>
                             </color>
                            </brush>
                           </colorrole>
                          </disabled>
                         </palette>
                        </property>
                        <property name="styleSheet">
                         <string notr="true">QPushButton
{
background-color: rgb(24,158,87);
border-radius: 5px;
font: bold 14px;
padding: 5px;
color: rgb(255,255,255);
} </string>
                        </property>
                        <property name="text">
                         <string>Genera Spreasheet</string>
                        </property>
                       </widget>
                      </item>
                     </layout>
                    </widget>
                   </item>
                   <item row="0" column="1">
                    <widget class="QGroupBox" name="groupBox_9">
                     <property name="styleSheet">
                      <string notr="true">background-color: rgb(230,231,232);
margin-top: 0.5em;
font: 16px;
color:  rgb(97,98,97);
border: 0px solid white;
padding: 14;
</string>
                     </property>
                     <property name="title">
                      <string>Google SS Generados</string>
                     </property>
                     <layout class="QGridLayout" name="gridLayout_11">
                      <item row="0" column="0">
                       <widget class="QListWidget" name="listWidgetPochtecaHistorial">
                        <property name="styleSheet">
                         <string notr="true">font: 11px;
color: rgb(97,98,97);
border: 0px solid rgba(143, 234, 79,90);
background-color: rgb(255,255,255);
</string>
                        </property>
                        <property name="frameShape">
                         <enum>QFrame::NoFrame</enum>
                        </property>
                       </widget>
                      </item>
                     </layout>
                    </widget>
                   </item>
                  </layout>
                 </widget>
                 <widget class="QWidget" name="tab_13">
                  <attribute name="title">
                   <string>Destinos</string>
                  </attribute>
                  <layout class="QGridLayout" name="gridLayout_54">
                   <item row="0" column="0">
                    <widget class="QGroupBox" name="groupBox_36">
                     <property name="styleSheet">
                      <string notr="true">background-color: rgb(230,231,232);
margin-top: 0.5em;
font: 16px;
color:  rgb(97,98,97);
border: 0px solid white;
padding: 14;
</string>
                     </property>
                     <property name="title">
                      <string>Añade Nuevas Direcciones (de... a...)</string>
                     </property>
                     <layout class="QGridLayout" name="gridLayout_53">
                      <item row="0" column="0">
                       <widget class="QTableWidget" name="tableWidgetPochtecaAnadeDe">
                        <property name="styleSheet">
                         <string notr="true">font: 11px;
color: rgb(97,98,97);
border: 0px solid rgba(143, 234, 79,90);
background-color: rgb(255,255,255);
</string>
                        </property>
                       </widget>
                      </item>
                      <item row="1" column="0">
                       <widget class="QTableWidget" name="tableWidgetPochtecaAnadeA">
                        <property name="styleSheet">
                         <string notr="true">font: 11px;
color: rgb(97,98,97);
border: 0px solid rgba(143, 234, 79,90);
background-color: rgb(255,255,255);
</string>
                        </property>
                       </widget>
                      </item>
                      <item row="2" column="0">
                       <widget class="QPushButton" name="pushButtonInterfasePochtecaAnadeDir">
                        <property name="palette">
                         <palette>
                          <active>
                           <colorrole role="WindowText">
                            <brush brushstyle="SolidPattern">
                             <color alpha="255">
                              <red>255</red>
                              <green>255</green>
                              <blue>255</blue>
                             </color>
                            </brush>
                           </colorrole>
                           <colorrole role="Button">
                            <brush brushstyle="SolidPattern">
                             <color alpha="255">
                              <red>24</red>
                              <green>158</green>
                              <blue>87</blue>
                             </color>
                            </brush>
                           </colorrole>
                           <colorrole role="Text">
                            <brush brushstyle="SolidPattern">
                             <color alpha="255">
                              <red>255</red>
                              <green>255</green>
                              <blue>255</blue>
                             </color>
                            </brush>
                           </colorrole>
                           <colorrole role="ButtonText">
                            <brush brushstyle="SolidPattern">
                             <color alpha="255">
                              <red>255</red>
                              <green>255</green>
                              <blue>255</blue>
                             </color>
                            </brush>
                           </colorrole>
                           <colorrole role="Base">
                            <brush brushstyle="SolidPattern">
                             <color alpha="255">
                              <red>24</red>
                              <green>158</green>
                              <blue>87</blue>
                             </color>
                            </brush>
                           </colorrole>
                           <colorrole role="Window">
                            <brush brushstyle="SolidPattern">
                             <color alpha="255">
                              <red>24</red>
                              <green>158</green>
                              <blue>87</blue>
                             </color>
                            </brush>
                           </colorrole>
                          </active>
                          <inactive>
                           <colorrole role="WindowText">
                            <brush brushstyle="SolidPattern">
                             <color alpha="255">
                              <red>255</red>
                              <green>255</green>
                              <blue>255</blue>
                             </color>
                            </brush>
                           </colorrole>
                           <colorrole role="Button">
                            <brush brushstyle="SolidPattern">
                             <color alpha="255">
                              <red>24</red>
                              <green>158</green>
                              <blue>87</blue>
                             </color>
                            </brush>
                           </colorrole>
                           <colorrole role="Text">
                            <brush brushstyle="SolidPattern">
                             <color alpha="255">
                              <red>255</red>
                              <green>255</green>
                              <blue>255</blue>
                             </color>
                            </brush>
                           </colorrole>
                           <colorrole role="ButtonText">
                            <brush brushstyle="SolidPattern">
                             <color alpha="255">
                              <red>255</red>
                              <green>255</green>
                              <blue>255</blue>
                             </color>
                            </brush>
                           </colorrole>
                           <colorrole role="Base">
                            <brush brushstyle="SolidPattern">
                             <color alpha="255">
                              <red>24</red>
                              <green>158</green>
                              <blue>87</blue>
                             </color>
                            </brush>
                           </colorrole>
                           <colorrole role="Window">
                            <brush brushstyle="SolidPattern">
                             <color alpha="255">
                              <red>24</red>
                              <green>158</green>
                              <blue>87</blue>
                             </color>
                            </brush>
                           </colorrole>
                          </inactive>
                          <disabled>
                           <colorrole role="WindowText">
                            <brush brushstyle="SolidPattern">
                             <color alpha="255">
                              <red>255</red>
                              <green>255</green>
                              <blue>255</blue>
                             </color>
                            </brush>
                           </colorrole>
                           <colorrole role="Button">
                            <brush brushstyle="SolidPattern">
                             <color alpha="255">
                              <red>24</red>
                              <green>158</green>
                              <blue>87</blue>
                             </color>
                            </brush>
                           </colorrole>
                           <colorrole role="Text">
                            <brush brushstyle="SolidPattern">
                             <color alpha="255">
                              <red>255</red>
                              <green>255</green>
                              <blue>255</blue>
                             </color>
                            </brush>
                           </colorrole>
                           <colorrole role="ButtonText">
                            <brush brushstyle="SolidPattern">
                             <color alpha="255">
                              <red>255</red>
                              <green>255</green>
                              <blue>255</blue>
                             </color>
                            </brush>
                           </colorrole>
                           <colorrole role="Base">
                            <brush brushstyle="SolidPattern">
                             <color alpha="255">
                              <red>24</red>
                              <green>158</green>
                              <blue>87</blue>
                             </color>
                            </brush>
                           </colorrole>
                           <colorrole role="Window">
                            <brush brushstyle="SolidPattern">
                             <color alpha="255">
                              <red>24</red>
                              <green>158</green>
                              <blue>87</blue>
                             </color>
                            </brush>
                           </colorrole>
                          </disabled>
                         </palette>
                        </property>
                        <property name="styleSheet">
                         <string notr="true">QPushButton
{
background-color: rgb(24,158,87);
border-radius: 5px;
font: bold 14px;
padding: 5px;
color: rgb(255,255,255);
} </string>
                        </property>
                        <property name="text">
                         <string>Añade Direcciones</string>
                        </property>
                       </widget>
                      </item>
                     </layout>
                    </widget>
                   </item>
                   <item row="0" column="1">
                    <widget class="QGroupBox" name="groupBox">
                     <property name="styleSheet">
                      <string notr="true">background-color: rgb(230,231,232);
margin-top: 0.5em;
font: 16px;
color:  rgb(97,98,97);
border: 0px solid white;
padding: 14;
</string>
                     </property>
                     <property name="title">
                      <string>Resultados añadidos</string>
                     </property>
                     <layout class="QGridLayout" name="gridLayout_60">
                      <item row="0" column="0" colspan="2">
                       <widget class="QTableWidget" name="tableWidgetPochtecaLatLong">
                        <property name="minimumSize">
                         <size>
                          <width>600</width>
                          <height>0</height>
                         </size>
                        </property>
                        <property name="palette">
                         <palette>
                          <active>
                           <colorrole role="WindowText">
                            <brush brushstyle="SolidPattern">
                             <color alpha="255">
                              <red>97</red>
                              <green>98</green>
                              <blue>97</blue>
                             </color>
                            </brush>
                           </colorrole>
                           <colorrole role="Button">
                            <brush brushstyle="SolidPattern">
                             <color alpha="255">
                              <red>255</red>
                              <green>255</green>
                              <blue>255</blue>
                             </color>
                            </brush>
                           </colorrole>
                           <colorrole role="Light">
                            <brush brushstyle="SolidPattern">
                             <color alpha="255">
                              <red>33</red>
                              <green>255</green>
                              <blue>6</blue>
                             </color>
                            </brush>
                           </colorrole>
                           <colorrole role="Midlight">
                            <brush brushstyle="SolidPattern">
                             <color alpha="255">
                              <red>204</red>
                              <green>102</green>
                              <blue>255</blue>
                             </color>
                            </brush>
                           </colorrole>
                           <colorrole role="Text">
                            <brush brushstyle="SolidPattern">
                             <color alpha="255">
                              <red>97</red>
                              <green>98</green>
                              <blue>97</blue>
                             </color>
                            </brush>
                           </colorrole>
                           <colorrole role="BrightText">
                            <brush brushstyle="SolidPattern">
                             <color alpha="255">
                              <red>128</red>
                              <green>0</green>
                              <blue>64</blue>
                             </color>
                            </brush>
                           </colorrole>
                           <colorrole role="ButtonText">
                            <brush brushstyle="SolidPattern">
                             <color alpha="255">
                              <red>97</red>
                              <green>98</green>
                              <blue>97</blue>
                             </color>
                            </brush>
                           </colorrole>
                           <colorrole role="Base">
                            <brush brushstyle="SolidPattern">
                             <color alpha="255">
                              <red>255</red>
                              <green>255</green>
                              <blue>255</blue>
                             </color>
                            </brush>
                           </colorrole>
                           <colorrole role="Window">
                            <brush brushstyle="SolidPattern">
                             <color alpha="255">
                              <red>255</red>
                              <green>255</green>
                              <blue>255</blue>
                             </color>
                            </brush>
                           </colorrole>
                          </active>
                          <inactive>
                           <colorrole role="WindowText">
                            <brush brushstyle="SolidPattern">
                             <color alpha="255">
                              <red>97</red>
                              <green>98</green>
                              <blue>97</blue>
                             </color>
                            </brush>
                           </colorrole>
                           <colorrole role="Button">
                            <brush brushstyle="SolidPattern">
                             <color alpha="255">
                              <red>255</red>
                              <green>255</green>
                              <blue>255</blue>
                             </color>
                            </brush>
                           </colorrole>
                           <colorrole role="Light">
                            <brush brushstyle="SolidPattern">
                             <color alpha="255">
                              <red>33</red>
                              <green>255</green>
                              <blue>6</blue>
                             </color>
                            </brush>
                           </colorrole>
                           <colorrole role="Midlight">
                            <brush brushstyle="SolidPattern">
                             <color alpha="255">
                              <red>204</red>
                              <green>102</green>
                              <blue>255</blue>
                             </color>
                            </brush>
                           </colorrole>
                           <colorrole role="Text">
                            <brush brushstyle="SolidPattern">
                             <color alpha="255">
                              <red>97</red>
                              <green>98</green>
                              <blue>97</blue>
                             </color>
                            </brush>
                           </colorrole>
                           <colorrole role="BrightText">
                            <brush brushstyle="SolidPattern">
                             <color alpha="255">
                              <red>128</red>
                              <green>0</green>
                              <blue>64</blue>
                             </color>
                            </brush>
                           </colorrole>
                           <colorrole role="ButtonText">
                            <brush brushstyle="SolidPattern">
                             <color alpha="255">
                              <red>97</red>
                              <green>98</green>
                              <blue>97</blue>
                             </color>
                            </brush>
                           </colorrole>
                           <colorrole role="Base">
                            <brush brushstyle="SolidPattern">
                             <color alpha="255">
                              <red>255</red>
                              <green>255</green>
                              <blue>255</blue>
                             </color>
                            </brush>
                           </colorrole>
                           <colorrole role="Window">
                            <brush brushstyle="SolidPattern">
                             <color alpha="255">
                              <red>255</red>
                              <green>255</green>
                              <blue>255</blue>
                             </color>
                            </brush>
                           </colorrole>
                          </inactive>
                          <disabled>
                           <colorrole role="WindowText">
                            <brush brushstyle="SolidPattern">
                             <color alpha="255">
                              <red>97</red>
                              <green>98</green>
                              <blue>97</blue>
                             </color>
                            </brush>
                           </colorrole>
                           <colorrole role="Button">
                            <brush brushstyle="SolidPattern">
                             <color alpha="255">
                              <red>255</red>
                              <green>255</green>
                              <blue>255</blue>
                             </color>
                            </brush>
                           </colorrole>
                           <colorrole role="Light">
                            <brush brushstyle="SolidPattern">
                             <color alpha="255">
                              <red>33</red>
                              <green>255</green>
                              <blue>6</blue>
                             </color>
                            </brush>
                           </colorrole>
                           <colorrole role="Midlight">
                            <brush brushstyle="SolidPattern">
                             <color alpha="255">
                              <red>204</red>
                              <green>102</green>
                              <blue>255</blue>
                             </color>
                            </brush>
                           </colorrole>
                           <colorrole role="Text">
                            <brush brushstyle="SolidPattern">
                             <color alpha="255">
                              <red>97</red>
                              <green>98</green>
                              <blue>97</blue>
                             </color>
                            </brush>
                           </colorrole>
                           <colorrole role="BrightText">
                            <brush brushstyle="SolidPattern">
                             <color alpha="255">
                              <red>128</red>
                              <green>0</green>
                              <blue>64</blue>
                             </color>
                            </brush>
                           </colorrole>
                           <colorrole role="ButtonText">
                            <brush brushstyle="SolidPattern">
                             <color alpha="255">
                              <red>97</red>
                              <green>98</green>
                              <blue>97</blue>
                             </color>
                            </brush>
                           </colorrole>
                           <colorrole role="Base">
                            <brush brushstyle="SolidPattern">
                             <color alpha="255">
                              <red>255</red>
                              <green>255</green>
                              <blue>255</blue>
                             </color>
                            </brush>
                           </colorrole>
                           <colorrole role="Window">
                            <brush brushstyle="SolidPattern">
                             <color alpha="255">
                              <red>255</red>
                              <green>255</green>
                              <blue>255</blue>
                             </color>
                            </brush>
                           </colorrole>
                          </disabled>
                         </palette>
                        </property>
                        <property name="styleSheet">
                         <string notr="true">font: 11px;
color: rgb(97,98,97);
border: 0px solid rgba(143, 234, 79,90);
background-color: rgb(255,255,255);
</string>
                        </property>
                       </widget>
                      </item>
                     </layout>
                    </widget>
                   </item>
                  </layout>
                 </widget>
                </widget>
               </item>
              </layout>
             </widget>
            </widget>
           </item>
           <item row="1" column="0">
            <widget class="QLabel" name="labelStatusBarCEDI_4">
             <property name="text">
              <string/>
             </property>
             <property name="pixmap">
              <pixmap resource="recursos.qrc">:/Img/arms_logo.png</pixmap>
             </property>
             <property name="alignment">
              <set>Qt::AlignCenter</set>
             </property>
            </widget>
           </item>
          </layout>
         </widget>
        </widget>
       </item>
      </layout>
     </widget>
    </item>
   </layout>
  </widget>
  <widget class="QMenuBar" name="menuBar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>1835</width>
     <height>22</height>
    </rect>
   </property>
  </widget>
  <widget class="QToolBar" name="mainToolBar">
   <attribute name="toolBarArea">
    <enum>TopToolBarArea</enum>
   </attribute>
   <attribute name="toolBarBreak">
    <bool>false</bool>
   </attribute>
  </widget>
  <widget class="QStatusBar" name="statusBar"/>
 </widget>
 <layoutdefault spacing="6" margin="11"/>
 <resources>
  <include location="recursos.qrc"/>
 </resources>
 <connections/>
</ui>
