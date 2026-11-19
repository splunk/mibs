#
# PySNMP MIB module CISCO-GGSN-GEO-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-GGSN-GEO-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 08:32:22 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
ModuleIdentity, TimeTicks, IpAddress, Bits, ObjectIdentity, NotificationType, Gauge32, Counter64, Unsigned32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Integer32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "TimeTicks", "IpAddress", "Bits", "ObjectIdentity", "NotificationType", "Gauge32", "Counter64", "Unsigned32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Integer32", "iso")
TextualConvention, DisplayString, TruthValue, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "TruthValue", "RowStatus")
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
mibBuilder.exportSymbols("CISCO-GGSN-GEO-MIB", cggsnGeoMIB=cggsnGeoMIB, cggsnGeoPassiveEntry=cggsnGeoPassiveEntry, cggsnGeogroups=cggsnGeogroups, cggsnGeoPassiveGroup=cggsnGeoPassiveGroup, PYSNMP_MODULE_ID=cggsnGeoMIB, cggsnGeoConformance=cggsnGeoConformance, cggsnGeoRowStatus=cggsnGeoRowStatus, cggsnGeoPassiveIfOnStdby=cggsnGeoPassiveIfOnStdby, cggsnGeoVRFEnabled=cggsnGeoVRFEnabled, cggsnGeoCompliance=cggsnGeoCompliance, cggsnGeoPassiveStdbyIfName=cggsnGeoPassiveStdbyIfName, cggsnGeoCompliances=cggsnGeoCompliances, cggsnGeoProcessNumber=cggsnGeoProcessNumber, cggsnGeoPassiveTable=cggsnGeoPassiveTable)
