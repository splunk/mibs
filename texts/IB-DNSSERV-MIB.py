#
# PySNMP MIB module IB-DNSSERV-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/infoblox/IB-DNSSERV-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:11:07 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint")
IbString, ibDNSServ = mibBuilder.importSymbols("IB-SMI-MIB", "IbString", "ibDNSServ")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, enterprises, Bits, TimeTicks, Integer32, MibIdentifier, Unsigned32, ObjectIdentity, Counter64, Gauge32, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ModuleIdentity, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "enterprises", "Bits", "TimeTicks", "Integer32", "MibIdentifier", "Unsigned32", "ObjectIdentity", "Counter64", "Gauge32", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ModuleIdentity", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ibDnsServMIBModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 32, 1))
ibDnsServMIBModule.setRevisions(('2011-07-13 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ibDnsServMIBModule.setRevisionsDescriptions(('Creation of the DNS Server MIB file',))
if mibBuilder.loadTexts: ibDnsServMIBModule.setLastUpdated('201107130000Z')
if mibBuilder.loadTexts: ibDnsServMIBModule.setOrganization('Infoblox')
if mibBuilder.loadTexts: ibDnsServMIBModule.setContactInfo('Please See IB-SMI-MIB.')
if mibBuilder.loadTexts: ibDnsServMIBModule.setDescription('This file defines the Infoblox DNS Server MIB.')
ibDnsServMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 32, 1, 1))
ibDnsServConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 32, 1, 1, 1))
ibDnsServConfigImplementIdent = MibScalar((1, 3, 6, 1, 4, 1, 32, 1, 1, 1, 1), IbString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibDnsServConfigImplementIdent.setStatus('current')
if mibBuilder.loadTexts: ibDnsServConfigImplementIdent.setDescription('The implementation identification string for\n                  the DNS server software in use on the system.')
mibBuilder.exportSymbols("IB-DNSSERV-MIB", ibDnsServConfig=ibDnsServConfig, ibDnsServConfigImplementIdent=ibDnsServConfigImplementIdent, PYSNMP_MODULE_ID=ibDnsServMIBModule, ibDnsServMIBObjects=ibDnsServMIBObjects, ibDnsServMIBModule=ibDnsServMIBModule)
