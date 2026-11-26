#
# PySNMP MIB module CISCO-GGSN-GEO-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-GGSN-GEO-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:06:59 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Counter64, TimeTicks, NotificationType, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, ModuleIdentity, IpAddress, Bits, Gauge32, MibIdentifier, Counter32, Unsigned32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "ModuleIdentity", "IpAddress", "Bits", "Gauge32", "MibIdentifier", "Counter32", "Unsigned32", "ObjectIdentity")
DisplayString, TruthValue, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "RowStatus", "TextualConvention")
cggsnGeoMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 724))
cggsnGeoMIB.setRevisions(('2010-02-19 00:00',))
if mibBuilder.loadTexts: cggsnGeoMIB.setLastUpdated('201002190000Z')
if mibBuilder.loadTexts: cggsnGeoMIB.setOrganization('Cisco Systems, Inc.')
cggsnGeoPassiveTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 724, 1), )
if mibBuilder.loadTexts: cggsnGeoPassiveTable.setStatus('current')
cggsnGeoPassiveEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 724, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "CISCO-GGSN-GEO-MIB", "cggsnGeoProcessNumber"))
if mibBuilder.loadTexts: cggsnGeoPassiveEntry.setStatus('current')
cggsnGeoProcessNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 724, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: cggsnGeoProcessNumber.setStatus('current')
cggsnGeoPassiveStdbyIfName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 724, 1, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cggsnGeoPassiveStdbyIfName.setStatus('current')
cggsnGeoPassiveIfOnStdby = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 724, 1, 1, 3), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cggsnGeoPassiveIfOnStdby.setStatus('current')
cggsnGeoVRFEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 724, 1, 1, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cggsnGeoVRFEnabled.setStatus('current')
cggsnGeoRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 724, 1, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cggsnGeoRowStatus.setStatus('current')
cggsnGeoConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 724, 2))
cggsnGeogroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 724, 2, 1))
cggsnGeoCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 724, 2, 2))
cggsnGeoCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 724, 2, 2, 1)).setObjects(("CISCO-GGSN-GEO-MIB", "cggsnGeoPassiveGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cggsnGeoCompliance = cggsnGeoCompliance.setStatus('current')
cggsnGeoPassiveGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 724, 2, 1, 1)).setObjects(("CISCO-GGSN-GEO-MIB", "cggsnGeoPassiveStdbyIfName"), ("CISCO-GGSN-GEO-MIB", "cggsnGeoPassiveIfOnStdby"), ("CISCO-GGSN-GEO-MIB", "cggsnGeoVRFEnabled"), ("CISCO-GGSN-GEO-MIB", "cggsnGeoRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cggsnGeoPassiveGroup = cggsnGeoPassiveGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-GGSN-GEO-MIB", cggsnGeoPassiveIfOnStdby=cggsnGeoPassiveIfOnStdby, cggsnGeoCompliance=cggsnGeoCompliance, cggsnGeoConformance=cggsnGeoConformance, cggsnGeoPassiveEntry=cggsnGeoPassiveEntry, cggsnGeoPassiveStdbyIfName=cggsnGeoPassiveStdbyIfName, cggsnGeoProcessNumber=cggsnGeoProcessNumber, cggsnGeoVRFEnabled=cggsnGeoVRFEnabled, cggsnGeogroups=cggsnGeogroups, cggsnGeoCompliances=cggsnGeoCompliances, PYSNMP_MODULE_ID=cggsnGeoMIB, cggsnGeoPassiveTable=cggsnGeoPassiveTable, cggsnGeoPassiveGroup=cggsnGeoPassiveGroup, cggsnGeoMIB=cggsnGeoMIB, cggsnGeoRowStatus=cggsnGeoRowStatus)
