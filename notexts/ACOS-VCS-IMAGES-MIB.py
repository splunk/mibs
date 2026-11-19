#
# PySNMP MIB module ACOS-VCS-IMAGES-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/a10/ACOS-VCS-IMAGES-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 08:30:03 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
acosSchema, = mibBuilder.importSymbols("A10-AX-MIB", "acosSchema")
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
InetAddressType, = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, IpAddress, ObjectIdentity, Unsigned32, ModuleIdentity, MibIdentifier, NotificationType, Integer32, Gauge32, iso, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "IpAddress", "ObjectIdentity", "Unsigned32", "ModuleIdentity", "MibIdentifier", "NotificationType", "Integer32", "Gauge32", "iso", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Bits")
PhysAddress, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "PhysAddress", "TextualConvention", "DisplayString")
vcsImagesModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 22610, 2, 4, 8, 16))
if mibBuilder.loadTexts: vcsImagesModule.setLastUpdated('200705071327Z')
if mibBuilder.loadTexts: vcsImagesModule.setOrganization('A10 Networks, Inc.')
images = MibIdentifier((1, 3, 6, 1, 4, 1, 22610, 2, 4, 8, 16, 1))
imagesOperImagesListTable = MibTable((1, 3, 6, 1, 4, 1, 22610, 2, 4, 8, 16, 1, 2), )
if mibBuilder.loadTexts: imagesOperImagesListTable.setStatus('current')
imagesOperImagesListEntry = MibTableRow((1, 3, 6, 1, 4, 1, 22610, 2, 4, 8, 16, 1, 2, 1), ).setIndexNames((0, "ACOS-VCS-IMAGES-MIB", "imagesOperImagesListSlotId"), (0, "ACOS-VCS-IMAGES-MIB", "imagesOperImagesListImagesListListId"))
if mibBuilder.loadTexts: imagesOperImagesListEntry.setStatus('current')
imagesOperImagesListSlotId = MibTableColumn((1, 3, 6, 1, 4, 1, 22610, 2, 4, 8, 16, 1, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: imagesOperImagesListSlotId.setStatus('current')
imagesOperImagesListImagesListListId = MibTableColumn((1, 3, 6, 1, 4, 1, 22610, 2, 4, 8, 16, 1, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: imagesOperImagesListImagesListListId.setStatus('current')
imagesOperImagesListType = MibTableColumn((1, 3, 6, 1, 4, 1, 22610, 2, 4, 8, 16, 1, 2, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: imagesOperImagesListType.setStatus('current')
imagesOperImagesListImagesName = MibTableColumn((1, 3, 6, 1, 4, 1, 22610, 2, 4, 8, 16, 1, 2, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: imagesOperImagesListImagesName.setStatus('current')
mibBuilder.exportSymbols("ACOS-VCS-IMAGES-MIB", imagesOperImagesListSlotId=imagesOperImagesListSlotId, imagesOperImagesListImagesName=imagesOperImagesListImagesName, imagesOperImagesListImagesListListId=imagesOperImagesListImagesListListId, imagesOperImagesListType=imagesOperImagesListType, imagesOperImagesListTable=imagesOperImagesListTable, vcsImagesModule=vcsImagesModule, imagesOperImagesListEntry=imagesOperImagesListEntry, images=images, PYSNMP_MODULE_ID=vcsImagesModule)
