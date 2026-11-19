#
# PySNMP MIB module CISCO-CAT6k-NAT-STAT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-CAT6k-NAT-STAT-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 14:35:14 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Integer32, Gauge32, MibIdentifier, NotificationType, Unsigned32, Counter64, ObjectIdentity, IpAddress, iso, Counter32, ModuleIdentity, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Integer32", "Gauge32", "MibIdentifier", "NotificationType", "Unsigned32", "Counter64", "ObjectIdentity", "IpAddress", "iso", "Counter32", "ModuleIdentity", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoCat6kNatStatMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 861))
ciscoCat6kNatStatMIB.setRevisions(('2019-06-11 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoCat6kNatStatMIB.setRevisionsDescriptions(('Inital version of ciscoNatMib',))
if mibBuilder.loadTexts: ciscoCat6kNatStatMIB.setLastUpdated('201906110000Z')
if mibBuilder.loadTexts: ciscoCat6kNatStatMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoCat6kNatStatMIB.setContactInfo('Cisco Systems\n                Customer Service\n                Postal: 170 W Tasman Drive\n                San Jose, CA  95134\n                USA\n                Tel: +1 800 553-NETS\n\n                E-mail: cs-cat6000@cisco.com')
if mibBuilder.loadTexts: ciscoCat6kNatStatMIB.setDescription('The cisco catalyst 6000 Nat stat mib provides information about NAT\n     platform specific statistics in the system')
ciscoCat6kNatStatMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 861, 1))
ciscoCat6kNatStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 861, 1, 2))
ciscoCat6kNatStatMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 861, 2))
ciscoCat6kNatStatMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 861, 2, 1))
ciscoCat6kNatStatMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 861, 2, 2))
ciscoCat6kNatStatGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 861, 2, 2, 1)).setObjects(("CISCO-CAT6k-NAT-STAT-MIB", "ciscoCat6kNatType"), ("CISCO-CAT6k-NAT-STAT-MIB", "ciscoCat6kNatNetFlowType"), ("CISCO-CAT6k-NAT-STAT-MIB", "ciscoCat6kNatFlowRecord"), ("CISCO-CAT6k-NAT-STAT-MIB", "ciscoCat6kNatDynamicEntryUtilization"), ("CISCO-CAT6k-NAT-STAT-MIB", "ciscoCat6kNatStaticEntryUtilization"), ("CISCO-CAT6k-NAT-STAT-MIB", "ciscoCat6kNatOtherEntryUtilization"), ("CISCO-CAT6k-NAT-STAT-MIB", "ciscoCat6kNatTotalEntryCount"), ("CISCO-CAT6k-NAT-STAT-MIB", "ciscoCat6kNatResourceUtilization"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCat6kNatStatGroup = ciscoCat6kNatStatGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoCat6kNatStatGroup.setDescription('A collection of objects providing\n        status of NAT statistics')
ciscoCat6kNatStatMIBComplianceVer1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 861, 2, 1, 1)).setObjects(("CISCO-CAT6k-NAT-STAT-MIB", "ciscoCat6kNatStatGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCat6kNatStatMIBComplianceVer1 = ciscoCat6kNatStatMIBComplianceVer1.setStatus('current')
if mibBuilder.loadTexts: ciscoCat6kNatStatMIBComplianceVer1.setDescription('The compliance statement for\n        CISCO-CAT6k-NAT-STAT-MIB')
class NatType(TextualConvention, Integer32):
    description = 'Type of NAT'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("static", 1), ("dynamic", 2), ("mixed", 3), ("other", 4))

class NetFlowType(TextualConvention, Integer32):
    description = 'Type of Netflow'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("layer3", 1), ("mixed", 2))

class NatBool(TextualConvention, Integer32):
    description = 'Boolean type in this mib'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("disabled", 0), ("enabled", 1))

ciscoCat6kNatType = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 861, 1, 2, 1), NatType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoCat6kNatType.setStatus('current')
if mibBuilder.loadTexts: ciscoCat6kNatType.setDescription('NAT type can be Static, Dynamic,  Mixed and other. Static \n\tshould be displayed when static rules are hit. \n    Dynamic should be displayed when dynamic rules are hit. \n    If traffic hits rmap/pat rules, it should display as Other.')
ciscoCat6kNatNetFlowType = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 861, 1, 2, 2), NetFlowType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoCat6kNatNetFlowType.setStatus('current')
if mibBuilder.loadTexts: ciscoCat6kNatNetFlowType.setDescription('Netflow type will be Layer-3 or Mixed. \n    If the rules are hit based only on Layer 3 information, \n    it should display as Layer-3.For static/dynamic nat it is L3,rmap\n    and Pat uses L4 info and it is considered as Mixed.')
ciscoCat6kNatFlowRecord = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 861, 1, 2, 3), NatBool()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoCat6kNatFlowRecord.setStatus('current')
if mibBuilder.loadTexts: ciscoCat6kNatFlowRecord.setDescription('This object shows whether ip nat create flow config is \n        enabled or not.\n        By default it will be in enabled state only.')
ciscoCat6kNatDynamicEntryUtilization = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 861, 1, 2, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoCat6kNatDynamicEntryUtilization.setStatus('current')
if mibBuilder.loadTexts: ciscoCat6kNatDynamicEntryUtilization.setDescription('This object gives total utilization of dynamic NAT entries \n        present in the system.')
ciscoCat6kNatStaticEntryUtilization = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 861, 1, 2, 5), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoCat6kNatStaticEntryUtilization.setStatus('current')
if mibBuilder.loadTexts: ciscoCat6kNatStaticEntryUtilization.setDescription('This object gives total utilization of static NAT entries \n        present in the system.')
ciscoCat6kNatOtherEntryUtilization = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 861, 1, 2, 6), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoCat6kNatOtherEntryUtilization.setStatus('current')
if mibBuilder.loadTexts: ciscoCat6kNatOtherEntryUtilization.setDescription('This object gives total utilization of other \n        NAT (PAT,RMAP,Etc.)\n        entries present in the system.')
ciscoCat6kNatTotalEntryCount = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 861, 1, 2, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoCat6kNatTotalEntryCount.setStatus('current')
if mibBuilder.loadTexts: ciscoCat6kNatTotalEntryCount.setDescription('This object gives consolidated count of static as well as \n        dynamic entries present in the system.')
ciscoCat6kNatResourceUtilization = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 861, 1, 2, 8), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoCat6kNatResourceUtilization.setStatus('current')
if mibBuilder.loadTexts: ciscoCat6kNatResourceUtilization.setDescription('Total system resource used by the system')
mibBuilder.exportSymbols("CISCO-CAT6k-NAT-STAT-MIB", ciscoCat6kNatFlowRecord=ciscoCat6kNatFlowRecord, NatType=NatType, PYSNMP_MODULE_ID=ciscoCat6kNatStatMIB, ciscoCat6kNatStatMIBObjects=ciscoCat6kNatStatMIBObjects, ciscoCat6kNatStatMIB=ciscoCat6kNatStatMIB, ciscoCat6kNatStatMIBComplianceVer1=ciscoCat6kNatStatMIBComplianceVer1, ciscoCat6kNatTotalEntryCount=ciscoCat6kNatTotalEntryCount, ciscoCat6kNatStatMIBGroups=ciscoCat6kNatStatMIBGroups, ciscoCat6kNatNetFlowType=ciscoCat6kNatNetFlowType, ciscoCat6kNatStatMIBConformance=ciscoCat6kNatStatMIBConformance, ciscoCat6kNatOtherEntryUtilization=ciscoCat6kNatOtherEntryUtilization, ciscoCat6kNatResourceUtilization=ciscoCat6kNatResourceUtilization, ciscoCat6kNatStatGroup=ciscoCat6kNatStatGroup, NetFlowType=NetFlowType, ciscoCat6kNatStatus=ciscoCat6kNatStatus, NatBool=NatBool, ciscoCat6kNatStaticEntryUtilization=ciscoCat6kNatStaticEntryUtilization, ciscoCat6kNatDynamicEntryUtilization=ciscoCat6kNatDynamicEntryUtilization, ciscoCat6kNatStatMIBCompliances=ciscoCat6kNatStatMIBCompliances, ciscoCat6kNatType=ciscoCat6kNatType)
