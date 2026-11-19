#
# PySNMP MIB module CISCO-ATM-TRAFFIC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-ATM-TRAFFIC-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 08:32:23 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
atmTrafficDescrParamEntry, = mibBuilder.importSymbols("ATM-MIB", "atmTrafficDescrParamEntry")
ciscoExperiment, = mibBuilder.importSymbols("CISCO-SMI", "ciscoExperiment")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
ModuleIdentity, TimeTicks, IpAddress, Bits, NotificationType, Gauge32, Counter64, Unsigned32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Counter32, ObjectIdentity, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "TimeTicks", "IpAddress", "Bits", "NotificationType", "Gauge32", "Counter64", "Unsigned32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Counter32", "ObjectIdentity", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoAtmTrafficExtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 10, 11))
ciscoAtmTrafficExtMIB.setRevisions(('2002-08-26 00:00', '2001-11-01 00:00', '1997-05-29 00:00',))
if mibBuilder.loadTexts: ciscoAtmTrafficExtMIB.setLastUpdated('200208260000Z')
if mibBuilder.loadTexts: ciscoAtmTrafficExtMIB.setOrganization('Cisco System Inc.')
ciscoAtmTrafficExtMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 11, 1))
ciscoAtmTrafficTypeExt = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 11, 1, 1))
ciscoAtmTrafficTableExt = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 11, 1, 2))
atmNoClpNoScrCdvt = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 10, 11, 1, 1, 1))
if mibBuilder.loadTexts: atmNoClpNoScrCdvt.setStatus('deprecated')
atmClpScrMbsCdvt = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 10, 11, 1, 1, 2))
if mibBuilder.loadTexts: atmClpScrMbsCdvt.setStatus('current')
atmNoClpScrMbsCdvt = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 10, 11, 1, 1, 3))
if mibBuilder.loadTexts: atmNoClpScrMbsCdvt.setStatus('current')
atmNoClpMcr = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 10, 11, 1, 1, 4))
if mibBuilder.loadTexts: atmNoClpMcr.setStatus('current')
atmNoClpMcrCdvt = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 10, 11, 1, 1, 5))
if mibBuilder.loadTexts: atmNoClpMcrCdvt.setStatus('current')
atmTrafficDescrParamExtTable = MibTable((1, 3, 6, 1, 4, 1, 9, 10, 11, 1, 2, 1), )
if mibBuilder.loadTexts: atmTrafficDescrParamExtTable.setStatus('current')
atmTrafficDescrParamExtEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 10, 11, 1, 2, 1, 1), )
atmTrafficDescrParamEntry.registerAugmentions(("CISCO-ATM-TRAFFIC-MIB", "atmTrafficDescrParamExtEntry"))
atmTrafficDescrParamExtEntry.setIndexNames(*atmTrafficDescrParamEntry.getIndexNames())
if mibBuilder.loadTexts: atmTrafficDescrParamExtEntry.setStatus('current')
atmTrafficExplicitServCategory = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 11, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("cbr", 1), ("vbrRt", 2), ("vbrNrt", 3), ("abr", 4), ("ubr", 5), ("notDef", 6))).clone('notDef')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: atmTrafficExplicitServCategory.setStatus('current')
atmTrafficDerivedServCategory = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 11, 1, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("cbr", 1), ("vbrRt", 2), ("vbrNrt", 3), ("abr", 4), ("ubr", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atmTrafficDerivedServCategory.setStatus('current')
atmTrafficDescriptorName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 10, 11, 1, 2, 1, 1, 3), SnmpAdminString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: atmTrafficDescriptorName.setStatus('current')
ciscoAtmTrafficExtMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 11, 3))
ciscoAtmTrafficExtMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 11, 3, 1))
ciscoAtmTrafficExtMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 11, 3, 2))
ciscoAtmTrafficExtMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 11, 3, 1, 1)).setObjects(("CISCO-ATM-TRAFFIC-MIB", "ciscoAtmTrafficTableExtMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAtmTrafficExtMIBCompliance = ciscoAtmTrafficExtMIBCompliance.setStatus('deprecated')
ciscoAtmTrafficExtMIBComplianceRev1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 10, 11, 3, 1, 2)).setObjects(("CISCO-ATM-TRAFFIC-MIB", "ciscoAtmTrafficTableExtMIBGroup"), ("CISCO-ATM-TRAFFIC-MIB", "ciscoAtmTrafficNmsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAtmTrafficExtMIBComplianceRev1 = ciscoAtmTrafficExtMIBComplianceRev1.setStatus('current')
ciscoAtmTrafficTableExtMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 11, 3, 2, 1)).setObjects(("CISCO-ATM-TRAFFIC-MIB", "atmTrafficExplicitServCategory"), ("CISCO-ATM-TRAFFIC-MIB", "atmTrafficDerivedServCategory"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAtmTrafficTableExtMIBGroup = ciscoAtmTrafficTableExtMIBGroup.setStatus('current')
ciscoAtmTrafficNmsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 10, 11, 3, 2, 2)).setObjects(("CISCO-ATM-TRAFFIC-MIB", "atmTrafficDescriptorName"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAtmTrafficNmsGroup = ciscoAtmTrafficNmsGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-ATM-TRAFFIC-MIB", ciscoAtmTrafficExtMIBGroups=ciscoAtmTrafficExtMIBGroups, atmTrafficDescrParamExtEntry=atmTrafficDescrParamExtEntry, atmClpScrMbsCdvt=atmClpScrMbsCdvt, atmTrafficDerivedServCategory=atmTrafficDerivedServCategory, ciscoAtmTrafficExtMIBComplianceRev1=ciscoAtmTrafficExtMIBComplianceRev1, ciscoAtmTrafficExtMIBCompliances=ciscoAtmTrafficExtMIBCompliances, atmNoClpMcr=atmNoClpMcr, atmNoClpMcrCdvt=atmNoClpMcrCdvt, atmNoClpNoScrCdvt=atmNoClpNoScrCdvt, ciscoAtmTrafficExtMIBCompliance=ciscoAtmTrafficExtMIBCompliance, ciscoAtmTrafficTableExtMIBGroup=ciscoAtmTrafficTableExtMIBGroup, ciscoAtmTrafficNmsGroup=ciscoAtmTrafficNmsGroup, PYSNMP_MODULE_ID=ciscoAtmTrafficExtMIB, ciscoAtmTrafficExtMIB=ciscoAtmTrafficExtMIB, atmNoClpScrMbsCdvt=atmNoClpScrMbsCdvt, atmTrafficDescrParamExtTable=atmTrafficDescrParamExtTable, ciscoAtmTrafficExtMIBObjects=ciscoAtmTrafficExtMIBObjects, atmTrafficExplicitServCategory=atmTrafficExplicitServCategory, atmTrafficDescriptorName=atmTrafficDescriptorName, ciscoAtmTrafficTypeExt=ciscoAtmTrafficTypeExt, ciscoAtmTrafficExtMIBConformance=ciscoAtmTrafficExtMIBConformance, ciscoAtmTrafficTableExt=ciscoAtmTrafficTableExt)
