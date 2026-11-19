#
# PySNMP MIB module CISCO-LEC-DATA-VCC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-LEC-DATA-VCC-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 08:33:06 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
atmVclVci, atmVclVpi = mibBuilder.importSymbols("ATM-MIB", "atmVclVci", "atmVclVpi")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
AtmLaneAddress, lecIndex = mibBuilder.importSymbols("LAN-EMULATION-CLIENT-MIB", "AtmLaneAddress", "lecIndex")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
NotificationType, MibIdentifier, iso, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Unsigned32, TimeTicks, IpAddress, Bits, Counter64, Gauge32, Integer32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "MibIdentifier", "iso", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Unsigned32", "TimeTicks", "IpAddress", "Bits", "Counter64", "Gauge32", "Integer32", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoLecDataVccMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 69))
ciscoLecDataVccMIB.setRevisions(('1997-01-06 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoLecDataVccMIB.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoLecDataVccMIB.setLastUpdated('9701060000Z')
if mibBuilder.loadTexts: ciscoLecDataVccMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoLecDataVccMIB.setContactInfo('       Cisco Systems\n                           Customer Service\n\n                   Postal: 170 W Tasman Drive\n                           San Jose, CA  95134\n                           USA\n\n                      Tel: +1 800 553-NETS\n\n                   E-mail: cs-atm@cisco.com')
if mibBuilder.loadTexts: ciscoLecDataVccMIB.setDescription("This MIB module is a Cisco extension to the ATM\n                Forum's LANE Client MIB.  This extension identifies\n                those VCCs which are being used to carry packets\n                sent on LANE Data Direct VCCs.")
ciscoLecDataVccMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 69, 1))
cLecDataDirectVcc = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 69, 1, 1))
cLecDataDirectVccTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 69, 1, 1, 1), )
if mibBuilder.loadTexts: cLecDataDirectVccTable.setStatus('current')
if mibBuilder.loadTexts: cLecDataDirectVccTable.setDescription('A table containing entries for all VCCs used as\n                LAN-Emulation Data Direct VCCs.')
cLecDataDirectVccEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 69, 1, 1, 1, 1), ).setIndexNames((0, "LAN-EMULATION-CLIENT-MIB", "lecIndex"), (0, "IF-MIB", "ifIndex"), (0, "ATM-MIB", "atmVclVpi"), (0, "ATM-MIB", "atmVclVci"))
if mibBuilder.loadTexts: cLecDataDirectVccEntry.setStatus('current')
if mibBuilder.loadTexts: cLecDataDirectVccEntry.setDescription('Each entry in this table represents a Data Direct VCC\n                for a particular Emulated LAN (ELAN):\n  \n                - the ELAN is identified by the lecIndex value.\n                - the VCC is identified by the combination of the\n                  interface (ifIndex, for which the corresponding\n                  ifType has the value atm(37)), the VPI (atmVclVpi)\n                  and the VCI (atmVclVci).\n\n                Entries appear in the table as a LANE client\n                establishes Data Direct VCs with other LANE clients\n                and are removed when the VCs are dropped.')
cLecDataDirectLocalAtmAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 69, 1, 1, 1, 1, 1), AtmLaneAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cLecDataDirectLocalAtmAddress.setStatus('current')
if mibBuilder.loadTexts: cLecDataDirectLocalAtmAddress.setDescription('The ATM Address of the local end of this Data Direct\n                VCC.')
cLecDataDirectRemoteAtmAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 69, 1, 1, 1, 1, 2), AtmLaneAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cLecDataDirectRemoteAtmAddress.setStatus('current')
if mibBuilder.loadTexts: cLecDataDirectRemoteAtmAddress.setDescription('The ATM Address of the remote end of this Data Direct\n                VCC.')
ciscoLecDataVccMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 69, 2))
ciscoLecDataVccMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 69, 2, 0))
ciscoLecDataVccMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 69, 3))
ciscoLecDataVccMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 69, 3, 1))
ciscoLecDataVccMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 69, 3, 2))
ciscoLecDataVccMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 69, 3, 1, 1)).setObjects(("CISCO-LEC-DATA-VCC-MIB", "ciscoLecDataVccBaseMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLecDataVccMIBCompliance = ciscoLecDataVccMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: ciscoLecDataVccMIBCompliance.setDescription('This module should be implemented by all Cisco\n                 devices supporting ATM LAN Emulation Clients.')
ciscoLecDataVccBaseMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 69, 3, 2, 1)).setObjects(("CISCO-LEC-DATA-VCC-MIB", "cLecDataDirectLocalAtmAddress"), ("CISCO-LEC-DATA-VCC-MIB", "cLecDataDirectRemoteAtmAddress"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoLecDataVccBaseMIBGroup = ciscoLecDataVccBaseMIBGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoLecDataVccBaseMIBGroup.setDescription("A collection of objects related to identifying\n                a LANE Client's Data Direct VCCs.")
mibBuilder.exportSymbols("CISCO-LEC-DATA-VCC-MIB", ciscoLecDataVccMIBCompliance=ciscoLecDataVccMIBCompliance, cLecDataDirectVccTable=cLecDataDirectVccTable, ciscoLecDataVccMIB=ciscoLecDataVccMIB, cLecDataDirectVcc=cLecDataDirectVcc, cLecDataDirectRemoteAtmAddress=cLecDataDirectRemoteAtmAddress, PYSNMP_MODULE_ID=ciscoLecDataVccMIB, ciscoLecDataVccMIBGroups=ciscoLecDataVccMIBGroups, cLecDataDirectLocalAtmAddress=cLecDataDirectLocalAtmAddress, cLecDataDirectVccEntry=cLecDataDirectVccEntry, ciscoLecDataVccMIBNotificationPrefix=ciscoLecDataVccMIBNotificationPrefix, ciscoLecDataVccBaseMIBGroup=ciscoLecDataVccBaseMIBGroup, ciscoLecDataVccMIBObjects=ciscoLecDataVccMIBObjects, ciscoLecDataVccMIBCompliances=ciscoLecDataVccMIBCompliances, ciscoLecDataVccMIBNotifications=ciscoLecDataVccMIBNotifications, ciscoLecDataVccMIBConformance=ciscoLecDataVccMIBConformance)
