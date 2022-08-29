# -*- coding: utf-8 -*-
"""
/***************************************************************************
 ODKConnectorDialog
                                 A QGIS plugin
 This plugIn connect you to your ODK instance and then pulls forms for you to use into QGIS
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2022-08-20
        git sha              : $Format:%H$
        copyright            : (C) 2022 by DDDev
        email                : demeveng@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import os

from qgis.PyQt import uic
from qgis.PyQt import QtWidgets

# This loads your .ui file so that PyQt can populate your plugin with the elements from Qt Designer
FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'odkConnector_dialog_base.ui'))


class ODKConnectorDialog(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(ODKConnectorDialog, self).__init__(parent)
        # Set up the user interface from Designer through FORM_CLASS.
        # After self.setupUi() you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)
        #connect button signals
        #self.connect.clicked.connect(self.connectionStatus)
        #self.previewData.clicked.connect(self.previewJsonData)
        #self.browsOutput.clicked.connect(self.fileBrowser)
        #self.singleGeo.toggled.connect(self.geometryState)
        #self.noGeometry.toggled.connect(self.noGeometryState)
        #self.addPcodes.toggled.connect(self.enablePcodes)
        #self.closeMain.clicked.connect(self.closeWindow)
        #self.runProcess.clicked.connect(self.run)