# -*- coding: utf-8 -*-
"""
/***************************************************************************
 ODKConnector
                                 A QGIS plugin
 This plugIn connect you to your ODK instance and then pulls forms for you to use into QGIS
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2022-08-20
        copyright            : (C) 2022 by DDDev
        email                : demeveng@gmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load ODKConnector class from file ODKConnector.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .odkConnector import ODKConnector
    return ODKConnector(iface)
