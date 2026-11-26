#
# PySNMP MIB module CISCO-DS0BUNDLE-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-DS0BUNDLE-EXT-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:06:58 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
dsx0BundleEntry, = mibBuilder.importSymbols("CISCO-DS0BUNDLE-MIB", "dsx0BundleEntry")
ciscoExperiment, = mibBuilder.importSymbols("CISCO-SMI", "ciscoExperiment")
InterfaceIndex, ifIndex = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex", "ifIndex")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Counter64, TimeTicks, NotificationType, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, ModuleIdentity, IpAddress, Bits, Gauge32, Unsigned32, MibIdentifier, Counter32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "ModuleIdentity", "IpAddress", "Bits", "Gauge32", "Unsigned32", "MibIdentifier", "Counter32", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoDs0BundleExtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 10, 33))
if mibBuilder.loadTexts: ciscoDs0BundleExtMIB.setLastUpdated('9806300000Z')
if mibBuilder.loadTexts: ciscoDs0BundleExtMIB.setOrganization('Cisco Systems')
ciscoDs0BundleExtMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 33, 1))
cdsx0BundleConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 33, 1, 1))
cdsx0BundleInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 33, 1, 2))
class Ds0ChannelList(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 4)

cdsx0BundleExtTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 33, 1, 1, 1), )
if mibBuilder.loadTexts: cdsx0BundleExtTable.setStatus('current')
cdsx0BundleExtEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 33, 1, 1, 1, 1), )
dsx0BundleEntry.registerAugmentions(("CISCO-DS0BUNDLE-EXT-MIB", "cdsx0BundleExtEntry"))
cdsx0BundleExtEntry.setIndexNames(*dsx0BundleEntry.getIndexNames())
if mibBuilder.loadTexts: cdsx0BundleExtEntry.setStatus('current')
cdsx0BundleExtDs1Index = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 33, 1, 1, 1, 1, 1), InterfaceIndex()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdsx0BundleExtDs1Index.setStatus('current')
cdsx0BundleExtChannelMap = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 33, 1, 1, 1, 1, 2), Ds0ChannelList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdsx0BundleExtChannelMap.setStatus('current')
cdsx0BundleExtEncapType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 33, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("atmFuni", 2), ("frameRelay", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdsx0BundleExtEncapType.setStatus('current')
cdsx0BundleExtChannelRate = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 33, 1, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("rate56", 1), ("rate64", 2))).clone('rate64')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cdsx0BundleExtChannelRate.setStatus('current')
cdsx0BundleUseTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 33, 1, 2, 1), )
if mibBuilder.loadTexts: cdsx0BundleUseTable.setStatus('current')
cdsx0BundleUseEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 33, 1, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: cdsx0BundleUseEntry.setStatus('current')
cdsx0BundleUseDs0Used = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 33, 1, 2, 1, 1, 1), Ds0ChannelList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdsx0BundleUseDs0Used.setStatus('current')
ciscoDs0BundleExtMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 33, 3))
ciscoDs0BundleExtMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 33, 3, 1))
ciscoDs0BundleExtMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 33, 3, 2))
ciscoDs0BundleExtMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 33, 3, 1, 1)).setObjects(("CISCO-DS0BUNDLE-EXT-MIB", "ciscoDs0BundleExtConfigGroup"), ("CISCO-DS0BUNDLE-EXT-MIB", "ciscoDs0BundleExtInfoGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDs0BundleExtMIBCompliance = ciscoDs0BundleExtMIBCompliance.setStatus('current')
ciscoDs0BundleExtConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 33, 3, 2, 1)).setObjects(("CISCO-DS0BUNDLE-EXT-MIB", "cdsx0BundleExtDs1Index"), ("CISCO-DS0BUNDLE-EXT-MIB", "cdsx0BundleExtChannelMap"), ("CISCO-DS0BUNDLE-EXT-MIB", "cdsx0BundleExtEncapType"), ("CISCO-DS0BUNDLE-EXT-MIB", "cdsx0BundleExtChannelRate"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDs0BundleExtConfigGroup = ciscoDs0BundleExtConfigGroup.setStatus('current')
ciscoDs0BundleExtInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 33, 3, 2, 2)).setObjects(("CISCO-DS0BUNDLE-EXT-MIB", "cdsx0BundleUseDs0Used"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoDs0BundleExtInfoGroup = ciscoDs0BundleExtInfoGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-DS0BUNDLE-EXT-MIB", cdsx0BundleExtEntry=cdsx0BundleExtEntry, cdsx0BundleExtDs1Index=cdsx0BundleExtDs1Index, ciscoDs0BundleExtMIBGroups=ciscoDs0BundleExtMIBGroups, cdsx0BundleExtChannelRate=cdsx0BundleExtChannelRate, cdsx0BundleInfo=cdsx0BundleInfo, ciscoDs0BundleExtMIBCompliance=ciscoDs0BundleExtMIBCompliance, cdsx0BundleExtTable=cdsx0BundleExtTable, ciscoDs0BundleExtMIBConformance=ciscoDs0BundleExtMIBConformance, cdsx0BundleConfig=cdsx0BundleConfig, cdsx0BundleUseEntry=cdsx0BundleUseEntry, cdsx0BundleExtChannelMap=cdsx0BundleExtChannelMap, cdsx0BundleExtEncapType=cdsx0BundleExtEncapType, cdsx0BundleUseDs0Used=cdsx0BundleUseDs0Used, Ds0ChannelList=Ds0ChannelList, ciscoDs0BundleExtMIBObjects=ciscoDs0BundleExtMIBObjects, ciscoDs0BundleExtMIB=ciscoDs0BundleExtMIB, ciscoDs0BundleExtInfoGroup=ciscoDs0BundleExtInfoGroup, PYSNMP_MODULE_ID=ciscoDs0BundleExtMIB, cdsx0BundleUseTable=cdsx0BundleUseTable, ciscoDs0BundleExtConfigGroup=ciscoDs0BundleExtConfigGroup, ciscoDs0BundleExtMIBCompliances=ciscoDs0BundleExtMIBCompliances)
