# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jan 27 2019)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MainWin
###########################################################################

class MainWin ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"磨机辅助控制系统", pos = wx.DefaultPosition, size = wx.Size( 800,500 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )


		bSizer1.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer5 = wx.BoxSizer( wx.VERTICAL )

		self.m_button11 = wx.Button( self, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.Size( 100,50 ), 0 )

		self.m_button11.SetBitmap( wx.Bitmap( u"/Volumes/work/github/machine_pi/btn.png", wx.BITMAP_TYPE_ANY ) )
		bSizer5.Add( self.m_button11, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"油泵启动", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )

		bSizer5.Add( self.m_staticText4, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer4.Add( bSizer5, 1, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )

		bSizer51 = wx.BoxSizer( wx.VERTICAL )

		self.m_button111 = wx.Button( self, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.Size( 100,50 ), 0 )

		self.m_button111.SetBitmap( wx.Bitmap( u"/Volumes/work/github/machine_pi/btn.png", wx.BITMAP_TYPE_ANY ) )
		bSizer51.Add( self.m_button111, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText41 = wx.StaticText( self, wx.ID_ANY, u"油泵停止", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText41.Wrap( -1 )

		bSizer51.Add( self.m_staticText41, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer4.Add( bSizer51, 1, wx.EXPAND, 5 )


		bSizer1.Add( bSizer4, 1, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer1.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		gSizer2 = wx.GridSizer( 0, 3, 0, 0 )

		bSizer52 = wx.BoxSizer( wx.VERTICAL )

		self.m_button112 = wx.Button( self, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.Size( 100,50 ), 0 )

		self.m_button112.SetBitmap( wx.Bitmap( u"/Volumes/work/github/machine_pi/btn.png", wx.BITMAP_TYPE_ANY ) )
		bSizer52.Add( self.m_button112, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText42 = wx.StaticText( self, wx.ID_ANY, u"横梁左移", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText42.Wrap( -1 )

		bSizer52.Add( self.m_staticText42, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		gSizer2.Add( bSizer52, 1, wx.EXPAND, 5 )

		bSizer521 = wx.BoxSizer( wx.VERTICAL )

		self.m_button1121 = wx.Button( self, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.Size( 100,50 ), 0 )

		self.m_button1121.SetBitmap( wx.Bitmap( u"/Volumes/work/github/machine_pi/btn.png", wx.BITMAP_TYPE_ANY ) )
		bSizer521.Add( self.m_button1121, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText421 = wx.StaticText( self, wx.ID_ANY, u"横梁暂停", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText421.Wrap( -1 )

		bSizer521.Add( self.m_staticText421, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		gSizer2.Add( bSizer521, 1, wx.EXPAND, 5 )

		bSizer522 = wx.BoxSizer( wx.VERTICAL )

		self.m_button1122 = wx.Button( self, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.Size( 100,50 ), 0 )

		self.m_button1122.SetBitmap( wx.Bitmap( u"/Volumes/work/github/machine_pi/btn.png", wx.BITMAP_TYPE_ANY ) )
		bSizer522.Add( self.m_button1122, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText422 = wx.StaticText( self, wx.ID_ANY, u"横梁右移", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText422.Wrap( -1 )

		bSizer522.Add( self.m_staticText422, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		gSizer2.Add( bSizer522, 1, wx.EXPAND, 5 )


		bSizer1.Add( gSizer2, 1, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer1.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		gSizer21 = wx.GridSizer( 0, 3, 0, 0 )

		bSizer523 = wx.BoxSizer( wx.VERTICAL )

		self.m_button1123 = wx.Button( self, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.Size( 100,50 ), 0 )

		self.m_button1123.SetBitmap( wx.Bitmap( u"/Volumes/work/github/machine_pi/btn.png", wx.BITMAP_TYPE_ANY ) )
		bSizer523.Add( self.m_button1123, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText423 = wx.StaticText( self, wx.ID_ANY, u"平台前进", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText423.Wrap( -1 )

		bSizer523.Add( self.m_staticText423, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		gSizer21.Add( bSizer523, 1, wx.EXPAND, 5 )

		bSizer5211 = wx.BoxSizer( wx.VERTICAL )

		self.m_button11211 = wx.Button( self, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.Size( 100,50 ), 0 )

		self.m_button11211.SetBitmap( wx.Bitmap( u"/Volumes/work/github/machine_pi/btn.png", wx.BITMAP_TYPE_ANY ) )
		bSizer5211.Add( self.m_button11211, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText4211 = wx.StaticText( self, wx.ID_ANY, u"平台暂停", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4211.Wrap( -1 )

		bSizer5211.Add( self.m_staticText4211, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		gSizer21.Add( bSizer5211, 1, wx.EXPAND, 5 )

		bSizer5221 = wx.BoxSizer( wx.VERTICAL )

		self.m_button11221 = wx.Button( self, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.Size( 100,50 ), 0 )

		self.m_button11221.SetBitmap( wx.Bitmap( u"/Volumes/work/github/machine_pi/btn.png", wx.BITMAP_TYPE_ANY ) )
		bSizer5221.Add( self.m_button11221, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_staticText4221 = wx.StaticText( self, wx.ID_ANY, u"平台后退", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4221.Wrap( -1 )

		bSizer5221.Add( self.m_staticText4221, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		gSizer21.Add( bSizer5221, 1, wx.EXPAND, 5 )


		bSizer1.Add( gSizer21, 1, wx.EXPAND, 5 )


		bSizer1.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


